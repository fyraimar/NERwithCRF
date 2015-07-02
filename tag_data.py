__author__ = 'yf'

import pycrfsuite

def tagging(model_name, test_data):
    tagger = pycrfsuite.Tagger()
    tagger.open(model_name)
    return [tagger.tag(xseq) for xseq in test_data]
