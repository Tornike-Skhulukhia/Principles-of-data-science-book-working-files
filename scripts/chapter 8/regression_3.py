from regression_ import bikes, LinearRegression
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import metrics

feature_cols = ['temp']
X = bikes[feature_cols]
y = bikes['count']

x_train, x_test, y_train, y_test = train_test_split(X, y)
linreg = LinearRegression().fit(x_train, y_train)

# try with temperature only
y_pred = linreg.predict(x_test)
print('RMSE = ', np.sqrt(metrics.mean_squared_error(y_pred, y_test)))

# add more features
feature_cols.extend(['windspeed', 'humidity'])
X = bikes[feature_cols]

x_train, x_test, y_train, y_test = train_test_split(X, y)
linreg = LinearRegression().fit(x_train, y_train)

# usually is worse by few points
y_pred = linreg.predict(x_test)
print('RMSE with temparature, windspeed and humidity = ',
       np.sqrt(metrics.mean_squared_error(y_pred, y_test)))

# null model
hourly_avg = bikes['count'].mean()
y_pred = [hourly_avg] * bikes.shape[0]

print("RMSE with null model = ",
     np.sqrt(metrics.mean_squared_error(y_pred, y)))
