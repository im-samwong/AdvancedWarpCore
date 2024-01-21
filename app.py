from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from joblib import load

# Define the time_to_seconds function
def time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds

# Load the model and preprocessors
model = load('mlp_regressor_model.joblib')
scaler = load('scaler.joblib')
encoders = {col: load(f'{col}_encoder.joblib') for col in ['PLAYER_ROLE', 'SERVER_NAME', 'MATCHMAKING_OUTCOME', 'MATCHMAKING_DAY_OF_WEEK']}

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Expecting JSON data with structure: {'PLAYER_ROLE': value, 'PARTY_SIZE': value, ...}
        # Example:
        # {
        #     "PLAYER_ROLE": "Survivor",
        #     "PARTY_SIZE": 4,
        #     "SERVER_NAME": "us-west-2",
        #     "MMR_GROUP_DECILE": 8,
        #     "MATCHMAKING_OUTCOME": "success",
        #     "MATCHMAKING_ATTEMPT_START_TIME_UTC": "3:09:31",
        #     "MATCHMAKING_DAY_OF_WEEK": "Mon"
        # }
        data = request.json
        data_df = pd.DataFrame(data, index=[0])

        # Label encode and transform data
        for col in encoders:
            if col in data_df.columns:
                data_df[col] = encoders[col].transform(data_df[col])

        data_df['MATCHMAKING_ATTEMPT_START_TIME_UTC'] = data_df['MATCHMAKING_ATTEMPT_START_TIME_UTC'].apply(time_to_seconds)

        print(data_df)

        # Ensure the input data matches the feature order expected by the model
        X_scaled = scaler.transform(data_df)

        # Make predictions
        predictions = model.predict(X_scaled)
        return jsonify({'predictions': predictions.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/add', methods=['POST'])
def add_five():
    data = request.json
    number = data['number']
    result = number + 5
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
