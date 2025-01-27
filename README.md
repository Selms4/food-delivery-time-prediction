
# Food Delivery Time Prediction

## Project Overview
This project is an AI-powered agent developed as part of a university project. It predicts food delivery times based on various factors like distance, weather, traffic levels, vehicle type, and courier experience. The goal is to apply machine learning techniques to optimize delivery operations and provide actionable insights.



## Project Structure

The project is structured as follows:
```
├── backend/
│   └── app.py               # Backend API built with Flask
├── data/
│   └── Dataset.csv          # Dataset for training and evaluation
├── frontend/
│   ├── index.html           # Frontend interface
│   ├── styles.css           # Frontend styling
│   └── styles.js            # Frontend functionality
├── models/
│   ├── model_delivery_time.joblib  # Trained machine learning model
│   └── preprocessor.joblib        # Preprocessing pipeline
├── notebooks/
│   └── delivery_time_prediction.ipynb  # Jupyter Notebook for analysis and model training
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation

```

## Key Features
- **Data Analysis**: Explore the dataset and visualize key patterns affecting delivery time.
- **Machine Learning**: Use RandomForestRegressor for predictions.
- **Backend API**: Flask-based API to serve predictions and recommendations.
- **Frontend Interface**: Simple user interface to interact with the API.
- **Recommendations**: Generate advice to improve delivery efficiency.

## Dataset
The dataset is sourced from [Kaggle](https://www.kaggle.com/datasets/denkuznetz/food-delivery-time-prediction/data) and contains the following key features:
- **Distance_km**: Distance between the restaurant and the delivery address.
- **Weather**: Weather conditions (e.g., Clear, Rainy).
- **Traffic_Level**: Traffic levels (e.g., Low, Medium, High).
- **Vehicle_Type**: Type of vehicle used (e.g., Scooter, Bike).
- **Preparation_Time_min**: Time taken to prepare the order.
- **Courier_Experience_yrs**: Experience of the courier.
- **Delivery_Time_min**: Target variable, representing the delivery time in minutes.

## Setup Instructions
1. Clone this repository:
   ```bash
   git clone https://github.com/Selms4/food-delivery-time-prediction.git
   cd food-delivery-time-prediction
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the backend server:
   ```bash
   python backend/app.py
   ```
4. Open the `index.html` file in your browser to interact with the application.

## Backend API Endpoints
- **POST /predict**: Predict delivery time and provide recommendations.
  - Request Body (JSON):
    ```json
    {
      "Distance_km": 5,
      "Weather": "Clear",
      "Traffic_Level": "Low",
      "Time_of_Day": "Afternoon",
      "Vehicle_Type": "Scooter",
      "Preparation_Time_min": 15,
      "Courier_Experience_yrs": 2
    }
    ```
  - Response:
    ```json
    {
      "Delivery_Time_min": 25.5,
      "Advice": "In clear weather, scooter usage is ideal."
    }
    ```

## Technologies Used
- **Python**: Core programming language.
- **Flask**: Backend framework.
- **Pandas, Scikit-learn**: Data processing and machine learning.
- **Joblib**: Model persistence.
- **HTML, CSS, JavaScript**: Frontend development.

## Future Enhancements
- Add more advanced machine learning models for comparison.
- Improve the frontend interface for better user experience.
- Deploy the project on cloud platforms like AWS or Heroku.

