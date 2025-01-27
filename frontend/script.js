// Function to generate a random Order ID
function generateOrderID() {
    const orderId = Math.floor(100000 + Math.random() * 900000); // Generate a 6-digit ID
    document.getElementById("order_id").value = orderId;
}

// Function to guess delivery time
function guessDeliveryTime() {
    const formData = {
        Distance_km: parseFloat(document.getElementById("distance_km").value),
        Weather: document.getElementById("weather").value,
        Traffic_Level: document.getElementById("traffic_level").value,
        Time_of_Day: document.getElementById("time_of_day").value,
        Vehicle_Type: document.getElementById("vehicle_type").value,
        Preparation_Time_min: parseInt(document.getElementById("preparation_time").value),
        Courier_Experience_yrs: parseFloat(document.getElementById("courier_experience").value),
    };

    // Validate inputs
    if (isNaN(formData.Distance_km) || isNaN(formData.Preparation_Time_min) || isNaN(formData.Courier_Experience_yrs)) {
        alert("Please fill in all fields correctly.");
        return;
    }

    // Make a POST request to the backend API
    fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
    })
    .then((response) => response.json())
    .then((data) => {
        if (data.Delivery_Time_min) {
            document.getElementById("delivery_time").value = data.Delivery_Time_min;
            document.getElementById("prediction-result").textContent = `Predicted Delivery Time: ${data.Delivery_Time_min} minutes. Advice: ${data.Advice}`;
        } else {
            alert("Failed to fetch delivery time prediction.");
        }
    })
    .catch((error) => {
        console.error("Error:", error);
        alert("An error occurred while predicting delivery time.");
    });
}


// Ensure the DOM is fully loaded before running the script
document.addEventListener("DOMContentLoaded", function() {
    generateOrderID(); // Automatically generate order ID on page load
});
