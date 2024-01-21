import os
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from joblib import dump

def get_unique_folder(base_folder_name):
    """
    Append a number to the folder name if it already exists.
    Increment the number until a unique folder name is found.
    """
    counter = 1
    folder_name = base_folder_name
    while os.path.exists(folder_name):
        folder_name = f"{base_folder_name}_{counter}"
        counter += 1
    return folder_name

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

# Create a unique folder for the current run
unique_folder = get_unique_folder('model_output')
os.makedirs(unique_folder)

# Save the feature names for later use
with open(os.path.join(unique_folder, 'feature_names.txt'), 'w') as file:
    file.write('\n'.join(feature_names))

# Scaling features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Define the parameter grid for MLPRegressor
param_grid = {
    'activation': ['logistic', 'tanh', 'relu'],
    'hidden_layer_sizes': [(30, 50), (5, 5, 5), (100, 100)],
    'solver': ['adam', 'sgd']
}

# Create GridSearchCV object for MLPRegressor
grid_search = GridSearchCV(estimator=MLPRegressor(max_iter=1000), param_grid=param_grid, verbose=2, n_jobs=-1)

# Train the model
grid_search.fit(X_train, y_train)

# Save the best model in the unique folder
model_filename = os.path.join(unique_folder, 'mlp_regressor_model.joblib')
dump(grid_search.best_estimator_, model_filename)

# Save the scaler in the unique folder
scaler_filename = os.path.join(unique_folder, 'scaler.joblib')
dump(scaler, scaler_filename)

# Save the label encoders in the unique folder
for col in categorical_columns:
    encoder_filename = os.path.join(unique_folder, f'{col}_encoder.joblib')
    dump(encoders[col], encoder_filename)

# Make predictions with the best model
y_pred = grid_search.predict(X_test)

# Calculate and display evaluation metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print evaluation metrics
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')
