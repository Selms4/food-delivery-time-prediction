import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from joblib import dump, load
from flask import Flask, request, jsonify
from flask_cors import CORS

## Define the directory where models will be saved
model_directory = r"C:\Users\User SC\Documents\GitHub\food-delivery-time-prediction\models"

# Ensure the directory exists (optional, but good practice)
if not os.path.exists(model_directory):
    os.makedirs(model_directory)

# Function to load data
def load_data(file_path=r"C:\Users\User SC\Documents\GitHub\food-delivery-time-prediction\data\Dataset.csv"):
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    categorical_features = ['Weather', 'Traffic_Level', 'Time_of_Day', 'Vehicle_Type']
    preprocessor = ColumnTransformer(
        transformers=[('cat', OneHotEncoder(), categorical_features)],
        remainder='passthrough'
    )
    
    X = preprocessor.fit_transform(data[['Distance_km', 'Weather', 'Traffic_Level', 'Time_of_Day',
                                         'Vehicle_Type', 'Preparation_Time_min', 'Courier_Experience_yrs']])
    y = data['Delivery_Time_min']
    return train_test_split(X, y, test_size=0.2, random_state=42), preprocessor

def train_model(X_train, y_train):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save the model to the specified directory
    model_path = os.path.join(model_directory, 'model_delivery_time.joblib')
    dump(model, model_path)

def save_preprocessor(preprocessor):
    # Save the preprocessor to the specified directory
    preprocessor_path = os.path.join(model_directory, 'preprocessor.joblib')
    dump(preprocessor, preprocessor_path)

def predict_delivery(data):
    # Load the preprocessor and model from the specified directory
    preprocessor_path = os.path.join(model_directory, 'preprocessor.joblib')
    model_path = os.path.join(model_directory, 'model_delivery_time.joblib')

    preprocessor = load(preprocessor_path)
    model = load(model_path)
    
    input_data = pd.DataFrame([data])
    processed_data = preprocessor.transform(input_data)
    prediction = model.predict(processed_data)
    return prediction[0]

# Function to generate advice based on the input data
def generate_advice(data):
    advice = []

    # Weather and vehicle-related advice
    if data['Weather'] in ['Rainy', 'Foggy']:
        if data['Vehicle_Type'] in ['Scooter', 'Bike']:
            advice.append("Due to weather conditions, it is not recommended to use a bike or scooter. Consider using a car instead.")
        else:
            advice.append("The weather conditions are ideal for car transportation.")

    # Traffic-related advice
    if data['Traffic_Level'] in ['Medium', 'High']:
        if data['Vehicle_Type'] == 'Bike':
            advice.append("Due to high or medium traffic, a bike may not be the best option. Consider a scooter or car.")

    # Traffic and clear weather advice
    if data['Weather'] == 'Clear' and data['Traffic_Level'] in ['Medium', 'High']:
        if data['Vehicle_Type'] == 'Scooter':
            advice.append("In clear weather, but with medium or high traffic, a scooter is not ideal. Consider using a bike or car.")
        elif data['Vehicle_Type'] == 'Car':
            advice.append("In clear weather, with medium or high traffic, a bike may be a better option than a car. Consider using a bike instead.")

    # Advice for long preparation times
    if data['Preparation_Time_min'] > 30:
        advice.append("The preparation time seems a bit long, ensure everything is ready on time.")
    
    # Return the advice
    return " ".join(advice)

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    content = request.json
    prediction = predict_delivery(content)
    advice = generate_advice(content)  # Get advice based on input data
    return jsonify({'Delivery_Time_min': prediction, 'Advice': advice})

if __name__ == "__main__":
    data = load_data()
    (X_train, X_test, y_train, y_test), preprocessor = preprocess_data(data)
    
    # Save the preprocessor and model
    save_preprocessor(preprocessor)
    train_model(X_train, y_train)
    
    app.run(debug=True)
