__author__ = 'yiran.fei'

import os
import sys
import csv

from data_type import *

def read_labeled_data(path_to_data, logbook, labelbook):
    skip = []
    for file in os.listdir(path_to_data):
        with open(path_to_data + file) as f:
            if file.endswith(".txt"):
                logbook.add_log(file.replace(".txt", ""), f.read())
            if file.endswith(".ann"):
                to_add = f.readlines()
                if (to_add == []):
                    skip.append(file.replace(".ann", ""))
                else:
                    for line in to_add:
                        token = line.split("\t")
                        split_token = token[1].split(" ")
                        cat = split_token[0]
                        st = split_token[1]
                        ed = split_token[-1]
                        text = token[-1].strip()
                        nlabel = Token(file.replace(".ann", ""), text, st, ed)
                        labelbook.add_label(nlabel, cat)
    for s in skip:
        logbook.del_log(s)
    return

def read_unlabeled_data(path_to_data, logbook, n):
    i = 0
    csv.field_size_limit(sys.maxsize)
    for file in os.listdir(path_to_data):
        with open(path_to_data + file) as f:
            reader = csv.reader(f)
            for line in reader:
                logbook.add_log(i, line[0])
                i += 1
                if i >= n:
                    break
