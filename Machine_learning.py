#!/usr/bin/env python3
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create simple training data
# X is the input feature (e.g., hours studied), y is the target (e.g., test score)
X = np.array([[1], [2], [3], [4], [5]])  # 2D array for sklearn
y = np.array([2, 4, 6, 8, 10])           # Perfect linear relationship: y = 2x

# Step 2: Initialize and train the model
model = LinearRegression()
model.fit(X, y)

# Step 3: Make predictions
X_test = np.array([[6], [7]])
y_pred = model.predict(X_test)

# Step 4: Visualize the results
plt.scatter(X, y, color='blue', label='Training data')
plt.plot(X, model.predict(X), color='red', label='Model prediction')
plt.scatter(X_test, y_pred, color='green', label='Test predictions')
plt.xlabel('Input (X)')
plt.ylabel('Target (y)')
plt.title('Simple Linear Regression')
plt.legend()
plt.grid(True)
plt.show()
