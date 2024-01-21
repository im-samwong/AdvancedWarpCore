import os
import requests
import matplotlib.pyplot as plt

# Create a directory for the plots if it doesn't exist
plots_dir = 'model_plots_killer'
os.makedirs(plots_dir, exist_ok=True)

# Define the input data template
input_data_template = {
    "MATCHMAKING_ATTEMPT_START_TIME_UTC": "20:09:31",
    "MATCHMAKING_DAY_OF_WEEK": "",  # Placeholder for day of the week
    "PLAYER_ROLE": "Killer",
    "PARTY_SIZE": 1,
    "SERVER_NAME": "us-west-2",
    "MATCHMAKING_OUTCOME": "success",
    "MMR_GROUP_DECILE": 6
}

# Days of the week
days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# URLs for each model endpoint
urls = [
    'http://127.0.0.1:5000/predict',
    'http://127.0.0.1:5000/predict1',
    'http://127.0.0.1:5000/predict2',
    'http://127.0.0.1:5000/predict3'
]

# Store predictions for each model and each day
predictions = {url: [] for url in urls}

# Iterate over each day and each model endpoint
for day in days_of_week:
    input_data = input_data_template.copy()
    input_data['MATCHMAKING_DAY_OF_WEEK'] = day

    for url in urls:
        response = requests.post(url, json=input_data)
        if response.status_code == 200:
            predictions[url].append(response.json()['predictions'][0])
        else:
            predictions[url].append(None)  # Handle error cases

# Plotting the results and saving the plots
for url in urls:
    title_append = url.split('/')[-1]
    time = '20h'
    plt.figure()
    plt.plot(days_of_week, predictions[url], label=url.split('/')[-1])
    plt.xlabel('Day of the Week')
    plt.ylabel('Predictions')
    plt.title(f'Model Predictions by Day of the Week | {title_append} | {time}')
    plt.legend()

    # Save the plot to the specified directory
    plot_filename = f"{plots_dir}/plot_{url.split('/')[-1]}_{time}.png"
    plt.savefig(plot_filename)

    # Optionally, you can also display the plot
    # plt.show()

print("Plots are saved in the folder:", plots_dir)
