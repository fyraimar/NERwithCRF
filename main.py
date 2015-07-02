from data_reader import *
from pipeline import *

cats = ['A', 'B', 'C']
gazetteer_list = {k : set() for k in cats}

if __name__ == '__main__':
    path = "./data/123/"
    path2 = "./data/456/"
    path3 = "./data/789/"

    logbook = LogBook()
    labelbook = LabelBook()
    unlabeled_logbook = LogBook()

    read_labeled_data(path, logbook, labelbook)
    read_labeled_data(path2, logbook, labelbook)
    read_unlabeled_data(path3, unlabeled_logbook, 10000)

    sents = [log2sent(item[1], labelbook.get_label_by_lid(item[0]))
             for item in logbook.get_logbook_list()]
    unlabeled_sents = [log2sent(item[1], {})
                       for item in unlabeled_logbook.get_logbook_list()]
    unlabeled_logbooks = {i: unlabeled_sents[i*500:(i+1)*500]
                          for i in range(0, 20)}

    #random.shuffle(sents)
    train_sents = sents[:400]
    test_sents = sents[400:]

    build_gazetteer(gazetteer_list, train_sents)
    fdict = nltk.FreqDist(sent2corpus(train_sents))

    for i in range(0, int(sys.argv[1])):
        model_name = iterate(i, train_sents, test_sents, unlabeled_logbooks[i],
                             fdict, gazetteer_list)
