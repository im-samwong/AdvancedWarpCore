import random
from datetime import datetime, timedelta
import pandas as pd

def generate_special_scenario_data(day, role_to_increase, num_extra_attempts):
    data = []

    for _ in range(num_extra_attempts):
        match_id = f"{random.getrandbits(128):32x}"  # Generate a random match ID

        # Set time to evening hours of the specified day
        start_time = datetime.now().replace(hour=random.randint(19, 23), minute=random.randint(0, 59))
        start_time_str = start_time.strftime("%H:%M:%S")
        day_of_week = day

        # Randomly assign server and platform
        server = random.choice(['us-west-2', 'eu-central-1', 'us-east-1'])
        platform = random.choice(['steam', 'egs', 'ps5', 'xsx'])

        mmr_group = random.randint(1, 10)
        queue_duration = random.randint(25, 60)  # Longer queue duration due to imbalance

        # Generate data based on the imbalance scenario
        roles = ['Killer', 'Survivor', 'Survivor', 'Survivor', 'Survivor']
        if role_to_increase == 'Survivor':
            roles += ['Survivor'] * random.randint(1, 3)  # Additional survivors
        else:  # role_to_increase == 'Killer'
            roles = ['Killer'] * random.randint(2, 4) + roles[1:]  # Additional killers

        for role in roles:
            party_size = 1 if role == 'Killer' else random.randint(1, 4)
            outcome = 'success' if role != role_to_increase else random.choice(['success', 'player_cancelled'])

            data.append([match_id, start_time_str, day_of_week, role, party_size, server, platform, queue_duration, outcome, mmr_group])

    return data

def generate_matchmaking_data(num_matches, num_special_scenarios):
    data = []

    # Add regular matchmaking data
    for match_num in range(num_matches):
        match_id = f"{random.getrandbits(128):32x}"  # Generate a random match ID

        # Randomly choose a day and time for matchmaking attempt start
        day_of_week = random.choice(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
        start_time = datetime.now() - timedelta(days=random.randint(0, 7), hours=random.randint(0, 24), minutes=random.randint(0, 60))
        start_time_str = start_time.strftime("%H:%M:%S")

        # Randomly assign server and platform
        server = random.choice(['us-west-2', 'eu-central-1', 'us-east-1'])
        platform = random.choice(['steam', 'egs', 'ps5', 'xsx'])

        # Set MMR for the match
        mmr_group = random.randint(1, 10)

        # Determine if the matchmaking attempt is during non-peak hours (weekdays 9-17)
        is_non_peak_hours = day_of_week in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'] and 9 <= start_time.hour <= 17

        # Calculate queue duration based on MMR and non-peak hours
        if mmr_group in [1, 10]:
            queue_duration = random.randint(25, 60)  # High and low MMR
            if is_non_peak_hours:
                queue_duration += random.randint(5, 15)  # Additional wait time during non-peak hours
        else:  # Middle MMR
            queue_duration = random.randint(5, 25)

        # Generate data for 1 killer and 4 survivors
        for role in ['Killer'] + ['Survivor']*4:
            # Party size - assuming 1 for killer and random for survivors
            party_size = 1 if role == 'Killer' else random.randint(1, 4)

            # Matchmaking outcome
            outcome = 'success' if random.random() > 0.1 else 'player_cancelled'  # 90% chance of success

            data.append([match_id, start_time_str, day_of_week, role, party_size, server, platform, queue_duration, outcome, mmr_group])

    # Add special scenario data for Sunday and Wednesday nights
    data += generate_special_scenario_data('Sun', 'Survivor', num_special_scenarios)  # Sunday scenario
    data += generate_special_scenario_data('Wed', 'Killer', num_special_scenarios)   # Wednesday scenario

    return pd.DataFrame(data, columns=['MATCH_ID', 'MATCHMAKING_ATTEMPT_START_TIME_UTC', 'MATCHMAKING_DAY_OF_WEEK', 
                                       'PLAYER_ROLE', 'PARTY_SIZE', 'SERVER_NAME', 'PLATFORM', 
                                       'QUEUE_DURATION_IN_SECS', 'MATCHMAKING_OUTCOME', 'MMR_GROUP_DECILE'])

# Generate a sample dataset with special scenarios
sample_data = generate_matchmaking_data(100, 10)  # 100 regular matches and 10 special scenario attempts for each day
print(sample_data.head())

# To save the dataset to a CSV file
sample_data.to_csv('matchmaking_data_with_special_scenarios.csv', index=False)
