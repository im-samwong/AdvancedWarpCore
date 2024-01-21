import requests

# Define the input data in the expected JSON format
input_data = {
    "MATCHMAKING_ATTEMPT_START_TIME_UTC": "3:09:31",
    "MATCHMAKING_DAY_OF_WEEK": "Mon",
    "PLAYER_ROLE": "Survivor",
    "PARTY_SIZE": 1,
    "SERVER_NAME": "us-west-2",
    "MATCHMAKING_OUTCOME": "success",
    "MMR_GROUP_DECILE": 6
}

# Make a POST request to the Flask API
response = requests.post('http://127.0.0.1:5000/predict', json={key.strip(): value for key, value in input_data.items()})


# Print the response
print(response.json())
