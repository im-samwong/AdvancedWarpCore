import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from joblib import dump
import sys

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

# After preparing X
feature_names = X.columns.tolist()

# Save the feature names for later use
with open('feature_names.txt', 'w') as file:
    file.write('\n'.join(feature_names))

sys.exit()

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
grid_search = GridSearchCV(estimator=MLPRegressor(max_iter=1000), param_grid=param_grid, verbose=2, n_jobs=-1)

# Train the model
grid_search.fit(X_train, y_train)

# Save the best model
dump(grid_search.best_estimator_, 'mlp_regressor_model.joblib')

# Save the scaler
dump(scaler, 'scaler.joblib')

# Save the label encoders
for col in categorical_columns:
    dump(encoders[col], f'{col}_encoder.joblib')

# Make predictions with the best model
y_pred = grid_search.predict(X_test)

# Calculate and display evaluation metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print evaluation metrics
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')
