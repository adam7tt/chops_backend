import pandas as pd
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords

def process_word_count(l: list, min_ocurrences=5, min_word_length=5, limit=50):
    raw_text = ''
    for d in l:
        raw_text += ' ' + ' '.join([d['abstract'].replace('\n', ''), d['text'].replace('\n', '')])
    want_to_keep = []
    for key, val in get_word_count(raw_text).items():
        if len(str(key)) > min_word_length and val > min_ocurrences and key not in stopwords.words('english'):
            want_to_keep.append({'text': key, 'value': val})
    return pd.DataFrame(want_to_keep).sort_values('value', ascending=False)[:limit].to_json(orient='records')

def get_word_count(text):
    textblob = TextBlob(text)
    return textblob.word_counts