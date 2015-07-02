class Token:
    def __init__(self, rid, txt, st, ed):
        self.record_id = rid
        self.text = txt
        self.st_pos = st
        self.ed_pos = ed

class LabelBook:
    def __init__(self):
        self.labels = {}

    def add_label(self, token, label):
        self.labels[(token.record_id, token.st_pos, token.ed_pos)] = (label, token.text)

    def get_whole_label_by_lid(self, lid):
        ret = []
        for k, v in self.labels.iteritems():
            if k[0] == lid:
                ret.append((v[0], v[1]))
        return ret

    def get_label_by_lid(self, lid):
        ret  = {}
        for k, v in self.labels.iteritems():
            if k[0] == lid:
                words = v[1].split(" ")
                self.add_IO_label(words, v[0], ret)
        return ret

    def add_IOB_label(self, words, label, label_dict):
        for word in words:
            if word == words[0]:
                label_dict[word] = 'B-' + label
            else:
                label_dict[word] = 'I-' + label

    def add_IO_label(self, words, label, label_dict):
        for word in words:
            label_dict[word] = label

    def get_labelbook_length(self):
        return len(self.labels)

    def __str__(self):
        out = ""
        for k, v in self.labels.iteritems():
            to_print = [k[0], v[0], v[1], str(k[1]), str(k[2])]
            out += ",".join(to_print) + "\n"
        return out

class LogBook:
    def __init__(self):
        self.logs = {}

    def del_log(self, lid):
        self.logs.pop(lid, None)
        return

    def add_log(self, rid, log):
        self.logs[rid] = log
        return

    def get_log_by_lid(self, lid):
        return str(self.logs[lid])

    def get_logbook_list(self):
        ret =[]
        for k, v in self.logs.iteritems():
            ret.append((k, v))
        return ret

    def __str__(self):
        out = ""
        for k, v in self.logs.iteritems():
            out += str(k) + "," + str(v) + "\n"
        return out

    def get_length(self):
        return len(self.logs)

if __name__ == '__main__':
    pass
