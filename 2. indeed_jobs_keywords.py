from requests_html import HTMLSession
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd


s = HTMLSession()


# get postings
texts = []

for i in range(0, 30, 10):
    url = 'http://www.indeed.com/jobs?q=data+scientist&start='+str(i)
    resp = s.get(url)
    texts += [i.text for i in resp.html.find('div.summary')]
    print(i, "+")

# cool!
vect = CountVectorizer(ngram_range=(1,2), stop_words='english')
matrix = vect.fit_transform(texts)


print(len(vect.get_feature_names())[:20])
'''
    ['ability',
     'ability translate',
     'able',
     'able tell',
     'academic',
     'academic experience',
     'academic professional',
     'acceptable',
     'acceptable'...]
'''


word_or_phrase_and_counts = dict(zip(vect.get_feature_names(), matrix.toarray().sum(axis=0)))
print(word_or_phrase_and_counts)

# most commons ...
# pd.DataFrame(a.items()).sort_values(by=1, ascending=False)