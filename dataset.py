import random
from datetime import datetime, timedelta
import pandas as pd

def generate_matchmaking_data(num_matches):
    data = []

    for match_num in range(num_matches):
        match_id = f"{random.getrandbits(128):32x}"  # Generate a random match ID

        # Randomly choose a day and time for matchmaking attempt start
        day_of_week = random.choice(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
        start_time = datetime.now() - timedelta(days=random.randint(0, 7), hours=random.randint(0, 24), minutes=random.randint(0, 60))
        start_time_str = start_time.strftime("%H:%M:%S")

        # Randomly assign server
        server = random.choice(['us-west-2', 'eu-central-1', 'us-east-1'])
      

        # Set MMR for the match
        mmr_group = random.randint(1, 20)

        # Determine if the matchmaking attempt is during non-peak hours
        is_non_peak_hours = day_of_week in ['Mon', 'Tue', 'Wed', 'Thu', 'Sun'] or ((3 <= start_time.hour <= 12) and day_of_week in ['Fri', 'Sat'] )

        # Calculate queue duration based on MMR and non-peak hours
        if mmr_group in [1, 20]:
            queue_duration = random.randint(100, 200)  # High and low MMR
        if mmr_group in [2, 3, 19, 18]:
            queue_duration = random.randint(70, 140)  # High and low MMR
        else:
            queue_duration = random.randint(10, 45)
        if is_non_peak_hours:
            queue_duration += random.randint(20, 45)  # Additional wait time during non-peak hours

        if server == "us-east-1":
            queue_duration -= 10
        if server == 'us-west-1':
            queue_duration += 5

        # Generate platforms for parties in this match
        party_platforms = {1: random.choice(['steam', 'egs', 'ps5', 'xsx'])}
        for party_size in range(2, 5):
            available_platforms = ['steam', 'egs', 'ps5', 'xsx']
            if party_size - 1 in party_platforms:
                available_platforms.remove(party_platforms[party_size - 1])
            party_platforms[party_size] = random.choice(available_platforms)

        # Generate data for 1 killer and 4 survivors
        for role in ['Killer'] + ['Survivor']*4:
            # Party size - assuming 1 for killer and random for survivors
            party_size = 1 if role == 'Killer' else random.randint(1, 4)

            if role == "Killer":
                queue_duration += random.randint(30, 40) 
         
           
            

            # Assign platform based on party size
            platform = party_platforms[party_size]

            if party_size >= 1 and party_size < 4:
                queue_duration += random.randint(10, 20)  # Additional wait time for larger parties
            
            if party_size == 4:
                queue_duration -= random.randint(15, 25)  # Reduce wait time for complete parties

            # Matchmaking outcome
            outcome = 'success' 

            data.append([match_id, start_time_str, day_of_week, role, party_size, server, platform, queue_duration, outcome, mmr_group])

    return pd.DataFrame(data, columns=['MATCH_ID', 'MATCHMAKING_ATTEMPT_START_TIME_UTC', 'MATCHMAKING_DAY_OF_WEEK', 
                                       'PLAYER_ROLE', 'PARTY_SIZE', 'SERVER_NAME', 'PLATFORM', 
                                       'QUEUE_DURATION_IN_SECS', 'MATCHMAKING_OUTCOME', 'MMR_GROUP_DECILE'])

# Generate a sample dataset
sample_data = generate_matchmaking_data(10000)  # Generate data for 100 matches
print(sample_data.head())

# To save the dataset to a CSV file
sample_data.to_csv('matchmaking_data_default.csv', index=False)
