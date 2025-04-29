from flask import Flask, request, jsonify, send_from_directory
import numpy as np
import pandas as pd
import joblib
import traceback
import logging
import os

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Initialize the Flask app
app = Flask(__name__, static_folder='.')

# Load the saved Random Forest model
try:
    model = joblib.load('admission_model.pkl')
    logger.info("Model loaded successfully")
except Exception as e:
    logger.error(f"Error loading model: {str(e)}")
    logger.error(traceback.format_exc())
    model = None

# Serve the main page
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Serve static files
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

# Define a route to predict the chance of admit based on user input
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Check if model is loaded
        if model is None:
            return jsonify({'error': 'Model not loaded. Please check server logs.'}), 500

        # Get input data from the POST request
        if not request.is_json:
            return jsonify({'error': 'Request must be JSON'}), 400

        data = request.get_json()
        logger.debug(f"Received data: {data}")

        # Validate required fields
        required_fields = ['GRE Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR', 'CGPA', 'Research']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing required field: {field}'}), 400

        # Extract and validate values from the request
        try:
            gre_score = float(data['GRE Score'])
            toefl_score = float(data['TOEFL Score'])
            university_rating = float(data['University Rating'])
            sop = float(data['SOP'])
            lor = float(data['LOR'])
            cgpa = float(data['CGPA'])
            research = float(data['Research'])
        except ValueError as e:
            return jsonify({'error': f'Invalid value format: {str(e)}'}), 400

        # Validate value ranges
        if not (260 <= gre_score <= 340):
            return jsonify({'error': 'GRE Score must be between 260 and 340'}), 400
        if not (0 <= toefl_score <= 120):
            return jsonify({'error': 'TOEFL Score must be between 0 and 120'}), 400
        if not (1 <= university_rating <= 5):
            return jsonify({'error': 'University Rating must be between 1 and 5'}), 400
        if not (1 <= sop <= 5):
            return jsonify({'error': 'SOP must be between 1 and 5'}), 400
        if not (1 <= lor <= 5):
            return jsonify({'error': 'LOR must be between 1 and 5'}), 400
        if not (0 <= cgpa <= 10):
            return jsonify({'error': 'CGPA must be between 0 and 10'}), 400
        if research not in [0, 1]:
            return jsonify({'error': 'Research must be 0 or 1'}), 400

        # Prepare the input features for prediction
        input_data = np.array([[gre_score, toefl_score, university_rating, sop, lor, cgpa, research]])
        logger.debug(f"Input data shape: {input_data.shape}")

        # Make prediction
        prediction = model.predict(input_data)
        logger.debug(f"Prediction: {prediction}")

        # Return the prediction as a response
        return jsonify({'chance': float(prediction[0]) * 100 })

    except Exception as e:
        logger.error(f"Error during prediction: {str(e)}")
        logger.error(traceback.format_exc())
        return jsonify({'error': 'An unexpected error occurred. Please try again later.'}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


# We're using Flask to create a simple web service.

# We define a linear regression model using scikit-learn.

# The model is trained using sample data (you'll replace this with your actual dataset, or load the data dynamically).

# A /predict endpoint is created to take POST requests with user inputs (GRE score, TOEFL score, etc.) and return a predicted chance of admission.