__author__ = 'yf'

from pipeline_utils import *


def mix_labeled_unlabeled_data(labeled_train_x, labeled_train_y,unlabeled_train_x, unlabeled_train_y):
    return unlabeled_train_x + labeled_train_x, unlabeled_train_y + labeled_train_y

def build_gazetteer(gazetteer_list, sents):
    items = chain.from_iterable(sents)

    for item in items:
        label = item[2]
        word = item[0]
        if label == 'Z':
            continue

        gazetteer_list[label].add(word.lower())
        gazetteer_list[label].add(get_stemmed_word(word))

def update_gazetteer(gazetteer_list, train_x, train_y, st_pos, ed_pos = -1):
    if ed_pos == -1:
        ed_pos = len(train_x)
    add2gazetteer(train_x[st_pos:ed_pos], train_y[st_pos:ed_pos], gazetteer_list)

def get_data_with_features(data_x, freq_dict, gazetteer_list):
    return [sent2feature(sent, freq_dict, gazetteer_list) for sent in data_x]

def get_train_test_pair(train_sents, test_sents, fdict, gazetteer_list):
    train_x = [sent2feature(sent, fdict, gazetteer_list) for sent in train_sents]
    train_y = [sent2label(sent) for sent in train_sents]

    test_x = [sent2feature(sent, fdict, gazetteer_list) for sent in test_sents]
    test_y = [sent2label(sent) for sent in test_sents]

    return train_x, train_y, test_x, test_y

def add2gazetteer(utrain_x, utrain_y, gazetteer):
    x = list(chain.from_iterable(utrain_x))
    y = list(chain.from_iterable(utrain_y))

    for i in range(0, len(x)):
        if y[i] == "Z":
            continue
        gazetteer[y[i]].add(x[i][0].lower())
        gazetteer[y[i]].add(get_stemmed_word(x[i][0]))

