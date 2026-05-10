from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Step 1: create data
x = np.random.rand(20, 1)
y = 3 + 2*x + np.random.rand(20, 1)

# Step 2: create model
model = LinearRegression()

# Step 3: train model
model.fit(x, y)

# Step 4: predict
pred = model.predict(x)

# Step 5: evaluate
mse = mean_squared_error(y, pred)
r2 = r2_score(y, pred)

# Step 6: print results
print("MSE:", mse)
print("R2 Score:", r2)
print("Slope:", model.coef_)
print("Intercept:", model.intercept_)
