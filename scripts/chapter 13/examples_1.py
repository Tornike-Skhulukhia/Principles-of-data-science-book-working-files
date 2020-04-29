'''
    By default, not so accurate...
'''
from textblob import TextBlob

example_sentences = [
    "Telegraph - Bidzina Ivanishvili is world's most generous donor in the fight against COVID-19",
    "Four major cities of Georgia locked down again",
    "A young woman from the village of Rukhi was placed to the Kutaisi clinic with the symptoms of coronavirus",
    "Four more patients defeated coronavirus in Adjara",
    "1.16 million Euro for the development of agriculture in Georgia – the support of EU",
    "Fuel truck bomb kills 40 in northwestern Syria city",
    "We do not expect a radical increase as a result of aggressive testing at this stage - Ekaterine Tikaradze",
    "The President pardons 9 female prisoners on the occasion of the Annunciation Day",
    "Shalva Natelashvili visits socially vulnerable family",
]


def get_sentiment_score(sentence):
    return TextBlob(sentence).sentiment.polarity

for i in example_sentences:
    print(f'{get_sentiment_score(i):^7.3f} | {i}')
