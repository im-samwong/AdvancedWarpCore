import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load the dataset
data = pd.read_csv('matchmaking_data.csv')

# Label encode categorical variables
categorical_columns = ['PLAYER_ROLE', 'SERVER_NAME', 'MATCHMAKING_OUTCOME', 'MATCHMAKING_DAY_OF_WEEK']
encoders = {col: LabelEncoder() for col in categorical_columns}

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

# Scaling features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Define the parameter grid for MLPRegressor
param_grid = {
    'activation': ['logistic', 'tanh', 'relu'],
    'hidden_layer_sizes': [(30, 50), (5, 5, 5)],
    'solver': ['adam', 'sgd']
}

# Create GridSearchCV object for MLPRegressor
grid_search = GridSearchCV(estimator=MLPRegressor(max_iter=1000), param_grid=param_grid)

# Train the model
grid_search.fit(X_train, y_train)

# Save the best parameters to a text file
with open('best_params.txt', 'w') as file:
    file.write(str(grid_search.best_params_))

# Save the string representation of the best estimator to a text file
with open('best_estimator.txt', 'w') as file:
    file.write(str(grid_search.best_estimator_))

# Make predictions with the best model
y_pred = grid_search.predict(X_test)

# Calculate and display evaluation metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Save the evaluation metrics to a text file
with open('evaluation_metrics.txt', 'w') as file:
    file.write(f'Mean Squared Error: {mse}\n')
    file.write(f'R-squared: {r2}\n')

# Predicting for a new data point (example)
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

# Apply label encoding and scaling to the new data point
for col in categorical_columns:
    if col in new_data_point.columns:
        new_data_point[col] = encoders[col].transform(new_data_point[col])

new_data_point['MATCHMAKING_ATTEMPT_START_TIME_UTC'] = new_data_point['MATCHMAKING_ATTEMPT_START_TIME_UTC'].apply(time_to_seconds)
new_data_point_scaled = scaler.transform(new_data_point[X.columns])

# Predict queue wait time for the new data point
predicted_wait_time = grid_search.predict(new_data_point_scaled)

# Save the predicted queue wait time for the new data point
with open('predicted_wait_time.txt', 'w') as file:
    file.write(f'Predicted Queue Wait Time: {predicted_wait_time[0]} seconds')
