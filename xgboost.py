import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from xgboost import XGBRegressor

# assume df already loaded

# Step 1: create age column
current_year = datetime.now().year
df['age'] = current_year - df['year']

# Step 2: drop year
df = df.drop('year', axis=1)

# Step 3: split input/output
X = df.drop('price', axis=1)
y = df['price']

# Step 4: convert categorical
X = pd.get_dummies(X)

# Step 5: split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Step 6: model
model = XGBRegressor()

# Step 7: train
model.fit(X_train, y_train)

# Step 8: predict
y_pred = model.predict(X_test)

# Step 9: evaluation
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("R2:", r2_score(y_test, y_pred))
