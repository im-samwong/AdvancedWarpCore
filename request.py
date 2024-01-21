import requests

# Define the input data in the expected JSON format
input_data = {
    "PLAYER_ROLE": "Survivor",
    "PARTY_SIZE": 4,
    "SERVER_NAME": "us-west-2",
    "PLATFORM": "ps5",
    "MMR_GROUP_DECILE": 8,
    "MATCHMAKING_OUTCOME": "success",
    "MATCHMAKING_ATTEMPT_START_TIME_UTC": "3:09:31",
    "MATCHMAKING_DAY_OF_WEEK": "Mon"
}

# Make a POST request to the Flask API
response = requests.post('http://127.0.0.1:5000/predict', json=input_data)

# Print the response
print(response.json())
