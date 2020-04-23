from regression_ import bikes, LinearRegression
from sklearn import metrics
import numpy as np

feature_cols = ['temp']
X = bikes[feature_cols]
y = bikes['count']

linreg = LinearRegression().fit(X, y)

y_pred = linreg.predict(X)
# calculate RMSE
print("RMSE with just temperature = ", np.sqrt(metrics.mean_squared_error(y, y_pred)))

# add more features and compare RMSE
feature_cols = ['temp', 'humidity']
X = bikes[feature_cols]

linreg = LinearRegression().fit(X, y)
y_pred = linreg.predict(X)
print("RMSE with temperature and humidity = ", np.sqrt(metrics.mean_squared_error(y, y_pred)))


# we may be overfitting...
