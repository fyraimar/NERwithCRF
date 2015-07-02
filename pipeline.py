__author__ = 'yf'

from train_model import *
from evaluation import *
from tag_data import *
from prepare_data import *

def iterate(number, train_sents, test_sents, unlabeled_sents, fdict, gazetteer_list):

    model_name = str(number) + ".model"
    new_model_name = str(number + 1) + ".model"

    print '####round####: ', number

    if number == 0:
        count = 0
        for k, v in gazetteer_list.iteritems():
            count += len(v)
            print k,len(v)
        print 'total : ',count
        train_x, train_y, test_x, test_y = get_train_test_pair(train_sents, test_sents, fdict, gazetteer_list)
        train_model(train_x, train_y, new_model_name, {})
        pred_y = tagging(new_model_name, test_x)

        print_classification_report(test_y, pred_y)

        return new_model_name

    else:
        unlabeled_x = [sent2feature(sent, fdict, gazetteer_list) for sent in unlabeled_sents]
        pred_utrain_y = tagging(model_name, unlabeled_x)
        update_gazetteer(gazetteer_list, unlabeled_x, pred_utrain_y, 0)

        count = 0
        for k, v in gazetteer_list.iteritems():
            count += len(v)
            print k,len(v)
        print 'total : ',count

        unlabeled_x = [sent2feature(sent, fdict, gazetteer_list) for sent in unlabeled_sents]
        train_x, train_y, test_x, test_y = get_train_test_pair(train_sents, test_sents, fdict, gazetteer_list)
        new_train_x, new_train_y = mix_labeled_unlabeled_data(train_x, train_y, unlabeled_x, pred_utrain_y)

        train_model(new_train_x, new_train_y, new_model_name, {})

        new_test_x = [sent2feature(sent, fdict, gazetteer_list) for sent in test_sents]
        pred_y2 = tagging(new_model_name, new_test_x)

        print_classification_report(test_y, pred_y2)

        return new_model_name