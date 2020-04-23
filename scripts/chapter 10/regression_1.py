from regression_ import bikes, LinearRegression, sns, plt

feature_cols = ['temp', 'season', 'weather', 'humidity']
X = bikes[feature_cols]
y = bikes['count']

linreg = LinearRegression()
linreg.fit(X, y)

# pair results
results = list(zip(feature_cols, linreg.coef_))
for i, j in results: print(i, j)

# plot individual predictor and responses
sns.pairplot(bikes, x_vars=feature_cols, y_vars='count', kind='reg')
plt.show()

# weather line shows downward trend here, but is upward in previous model...

