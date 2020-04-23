import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('dark_background')
import seaborn as sns
from sklearn.linear_model import LinearRegression


bikes = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/bikeshare.csv')
# bikes.plot(kind='scatter', x='temp', y='count', alpha=0.2)

if __name__ == '__main__':
    # pedictors/feature_columns and responses
    feature_cols = ['temp']  # making prediction with this feature
    X = bikes[feature_cols]
    y = bikes['count']

    # create model
    linreg = LinearRegression()
    linreg.fit(X, y)  # fit model with our data

    # print coefficients
    print("B0 = ", linreg.intercept_)  # beta 0
    print("B1 = ", linreg.coef_)       # beta coefficients

    # make a prediction
    print("If the temperature is 20, model predicts ",
          linreg.predict([[20]]),
          "number of bike shares")  # different from book - [[]]

