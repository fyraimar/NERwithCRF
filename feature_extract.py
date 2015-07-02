from nltk.stem.porter import *

def add_features(sent, location, fdict, gazetteer_list, ret):
    stemmer = PorterStemmer()

    cur_word = sent[location][0].lower()

    #pos_tag = sent[location][1]

    ret.append(cur_word)

    '''
    ret.append("loc:" + str(location))

    ret.append("len:" + str(len(sent)))
    '''

    if (len(cur_word) > 2):
        ret.append("isEDend" + str(cur_word[-2:].lower() == "ed"))

    if (len(cur_word) > 2):
        ret.append("isESend" + str(cur_word[-2:].lower() == "es"))

    '''
    if "NN" in pos_tag:
        ret.append("isNurn:Y")
    else:
        ret.append("isNurn:N")
    '''
    '''ret.append("freq:" + str(fdict.get(cur_word, 0) > 100))'''

    ret.append("allletter:" + str(cur_word.isalpha()))

    ret.append("allnumber:" + str(cur_word.isdigit()))

    ret.append("has-:" + str("-" in cur_word))

    ret.append("has/:" + str("/" in cur_word))

    '''
    flag = False
    for c in cur_word:
        if c in string.punctuation:
            flag = True
    ret.append("hasPunc:" + str(flag))


    if (len(cur_word) >= 4):
        ret.append("pre:" + cur_word[:2])
        ret.append("suf:" + cur_word[-2:])
    else:
        ret.append("pre:" + "  ")
        ret.append("suf:" + "  ")
    '''

    for k, v in gazetteer_list.iteritems():
        if cur_word.lower() in gazetteer_list[k] or (stemmer.stem(cur_word.decode('utf-8', 'replace')) in gazetteer_list[k]):
            ret.append("in" + k + ":T")
        else:
            ret.append("in" + k + ":F")

    '''
    for k, v in gazetteer_list.iteritems():
        if (location >= len(sent) - 1) or (sent[location+1] not in gazetteer_list[k]):
            ret.append("NextIn" + k + ":F")
        else:
            ret.append("NextIn" + k + ":T")

    for k, v in gazetteer_list.iteritems():
        if (location <= 0) or (sent[location-1] not in gazetteer_list[k]):
            ret.append("PreIn" + k + ":F")
        else:
            ret.append("PreIn" + k + ":T")

    if location > 0:
        ret.append(sent[location-1][0] + " " + cur_word)
    else:
        ret.append(" " + cur_word)

    if location < len(sent) - 1:
        ret.append(cur_word + " " + sent[location+1][0])
    else:
        ret.append(cur_word + " ")
    '''

