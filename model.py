import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

# Load the dataset
data = pd.read_csv('matchmaking_data.csv')

# Label encode categorical variables
categorical_columns = ['PLAYER_ROLE', 'SERVER_NAME', 'MATCHMAKING_OUTCOME', 'MATCHMAKING_DAY_OF_WEEK']

# Initialize a dictionary to store the encoders for each categorical variable
encoders = {col: LabelEncoder() for col in categorical_columns}

# Apply label encoding to the dataset and store encoders
for col in categorical_columns:
    data[col] = encoders[col].fit_transform(data[col])

# Function to convert time string to seconds
def time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds

# Apply the time conversion function
data['MATCHMAKING_ATTEMPT_START_TIME_UTC'] = data['MATCHMAKING_ATTEMPT_START_TIME_UTC'].apply(time_to_seconds)

# Prepare features and target variable for training
X = data.drop(columns=['QUEUE_DURATION_IN_SECS', 'MATCH_ID', 'PLATFORM'])
y = data['QUEUE_DURATION_IN_SECS']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions and calculate metrics
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Absolute Error: {mae}')
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

# Process new data point after model evaluation
# Example prediction for a new data point (make sure to label encode this point)
new_data_point = pd.DataFrame({
    'PLAYER_ROLE': ['Survivor'], 
    'PARTY_SIZE': [4], 
    'SERVER_NAME': ['us-west-2'], 
    'PLATFORM': ['ps5'], 
    'MMR_GROUP_DECILE': [8],
    'MATCHMAKING_OUTCOME': ['success'],
    'MATCHMAKING_ATTEMPT_START_TIME_UTC': ['3:09:31'],
    'MATCHMAKING_DAY_OF_WEEK': ['Mon']
})

# Apply label encoding to the new data point using the stored encoders
for col in categorical_columns:
    if col in new_data_point.columns:
        new_data_point[col] = encoders[col].transform(new_data_point[col])

# Apply the time conversion function to new data point
new_data_point['MATCHMAKING_ATTEMPT_START_TIME_UTC'] = new_data_point['MATCHMAKING_ATTEMPT_START_TIME_UTC'].apply(time_to_seconds)

# Ensure new_data_point has the same columns, in the same order as X used for training
new_data_point_for_prediction = new_data_point[X.columns]

# Make predictions for the new data point
predicted_wait_time = model.predict(new_data_point_for_prediction)

print(f'Predicted Queue Wait Time: {predicted_wait_time[0]} seconds')
