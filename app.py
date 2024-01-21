from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from joblib import load

# Define the time_to_seconds function
def time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds

app = Flask(__name__)
CORS(app)

# Function to load model and preprocessors for a given folder
def load_model_and_preprocessors(model_folder):
    model = load(f'{model_folder}/mlp_regressor_model.joblib')
    scaler = load(f'{model_folder}/scaler.joblib')
    encoders = {col: load(f'{model_folder}/{col}_encoder.joblib') for col in ['PLAYER_ROLE', 'SERVER_NAME', 'MATCHMAKING_OUTCOME', 'MATCHMAKING_DAY_OF_WEEK']}
    return model, scaler, encoders

# Load models and preprocessors for different folders
models = {}
models['model_output'], models['scaler'], models['encoders'] = load_model_and_preprocessors('model_output')
models['model_output_1'], models['scaler_1'], models['encoders_1'] = load_model_and_preprocessors('model_output_1')
models['model_output_2'], models['scaler_2'], models['encoders_2'] = load_model_and_preprocessors('model_output_2')
models['model_output_3'], models['scaler_3'], models['encoders_3'] = load_model_and_preprocessors('model_output_3')

# Define a function to process prediction requests
def process_predict_request(model, scaler, encoders):
    try:
        data = request.json
        data_df = pd.DataFrame(data, index=[0])

        for col in encoders:
            if col in data_df.columns:
                data_df[col] = encoders[col].transform(data_df[col])

        data_df['MATCHMAKING_ATTEMPT_START_TIME_UTC'] = data_df['MATCHMAKING_ATTEMPT_START_TIME_UTC'].apply(time_to_seconds)

        X_scaled = scaler.transform(data_df)
        predictions = model.predict(X_scaled)
        return jsonify({'predictions': predictions.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)})

# Define endpoints
@app.route('/predict', methods=['POST'])
def predict():
    return process_predict_request(models['model_output'], models['scaler'], models['encoders'])

@app.route('/predict1', methods=['POST'])
def predict1():
    return process_predict_request(models['model_output_1'], models['scaler_1'], models['encoders_1'])

@app.route('/predict2', methods=['POST'])
def predict2():
    return process_predict_request(models['model_output_2'], models['scaler_2'], models['encoders_2'])

@app.route('/predict3', methods=['POST'])
def predict3():
    return process_predict_request(models['model_output_3'], models['scaler_3'], models['encoders_3'])

    
@app.route('/add', methods=['POST'])
def add_five():
    data = request.json
    number = data['number']
    result = number + 5
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
