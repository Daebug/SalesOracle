import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

# Load preprocessed data (assuming data.csv is in the current directory)
data = pd.read_csv('data.csv')

# Split data into features (X) and target variable (y)
X = data[['sales_revenue', 'cost_of_goods_sold', 'operating_expenses']]
y = data['success_rate']

# Train-test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

# Evaluate the model
train_rmse = mean_squared_error(y_train, y_pred_train, squared=False)
test_rmse = mean_squared_error(y_test, y_pred_test, squared=False)

print("Training RMSE:", train_rmse)
print("Testing RMSE:", test_rmse)

# Save the trained model to a pickle file
joblib.dump(model, 'trained_model.pkl')
