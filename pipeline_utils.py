__author__ = 'yf'

from itertools import chain

import nltk
from nltk.corpus import stopwords

from feature_extract import *


def log2sent(log, labels):
    ret = []
    tags = {}
    for token in log.split(" "):
        label = labels.get(token, None)
        if label == None:
            label = "Z"

        tag = tags.get(token, None)
        if tag == None:
            tag = "NULL"

        ret.append((token, tag, label))
    return ret

def get_pos_tag(sent):
    ret = {}
    text = nltk.word_tokenize(sent.decode('utf-8', 'replace'))
    lists = nltk.pos_tag(text)
    for item in lists:
        ret[item[0]] = item[1]

    return ret

def sent2feature(sent, fdict, gazetteer_list):
    return [word2feature(sent, i, fdict, gazetteer_list)
            for i in range(0, len(sent))]

def word2feature(sent, location, fdict, gazetteer_list):
    ret = []
    add_features(sent, location, fdict, gazetteer_list, ret)
    return ret

def sent2label(sent):
    return [label for token, tag, label in sent]

def sent2corpus(sents):
    lists = chain.from_iterable(sents)
    return [token for token, tag, label in lists]

def is_stopword(word):
    stop = stopwords.words('english')
    return word.lower() in stop

def get_stemmed_word(word):
    stemmer = PorterStemmer()
    return stemmer.stem(word.lower().decode('utf-8', 'replace'))



