import pandas as pd
import sklearn
from sklearn.feature_extraction.text import CountVectorizer

train_simple = ['call you tonight',
                'Call me a cab',
                'please call me... PLEASE 44!']

vc = CountVectorizer()
# creates dtm - .fit_transform
train_simple_dtm = vc.fit_transform(train_simple)

df = pd.DataFrame(train_simple_dtm.toarray(),
                  columns=vc.get_feature_names())
print(df, "\n")

test_simple = ['Please don\'t call me']
test_simple_dtm = vc.transform(test_simple)

# uses existing dtm - .transform
# ! - vectorizer ignores new word - 'don\t' 
df_simple = pd.DataFrame(test_simple_dtm.toarray(),
                         columns=vc.get_feature_names())
print(df_simple)

