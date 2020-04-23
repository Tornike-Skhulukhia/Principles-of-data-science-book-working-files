# from nb_1 import df
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics


from info_ import no_duplicate_data
df = pd.DataFrame(no_duplicate_data)


x_train, x_test, y_train, y_test = train_test_split(df.title, df.category, test_size=0.1)

vc = CountVectorizer()

train_dtm = vc.fit_transform(x_train)
# print(repr(train_dtm))

test_dtm = vc.transform(x_test)
# print(repr(test_dtm))

nb = MultinomialNB()

nb.fit(train_dtm, y_train)

preds = nb.predict(test_dtm)

print(metrics.accuracy_score(y_test, preds))

print(nb.classes_)
print(metrics.confusion_matrix(y_test, preds))


