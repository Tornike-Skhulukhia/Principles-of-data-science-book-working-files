from regression_ import bikes, plt, pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics


bikes['above_average'] = bikes['count'] >= bikes['count'].mean()
bikes['hour'] = bikes['datetime'].apply(lambda x: int(x[11:13]))


def when_is_it(hour):
    if 5 <= hour < 11:  return "morning"
    if 11 <= hour < 16: return "afternoon"
    if 16 <= hour < 18: return "rush_hour"
    return "off_hours"

bikes['when_is_it'] = bikes['hour'].apply(when_is_it)

when_dummies = pd.get_dummies(bikes['when_is_it'], prefix='when_').iloc[:, 1:]


X = when_dummies
y = bikes['above_average']

x_train, x_test, y_train, y_test = train_test_split(X, y)

logreg = LogisticRegression()
logreg.fit(x_train, y_train)

score = logreg.score(x_test, y_test)
print(score)


