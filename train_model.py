__author__ = 'yf'

import pycrfsuite

def train_model(train_x, train_y, model_name, params = {}):
    trainer = pycrfsuite.Trainer(verbose=False)
    for xseq, yseq in zip(train_x, train_y):
        trainer.append(xseq, yseq)
    if params == {}:
        trainer.set_params({
            'c1': 0,   # coefficient for L1 penalty
            'c2': 0.01,  # coefficient for L2 penalty
            'max_iterations': 500,  # stop earlier
            'feature.possible_transitions': True,
        })
    else:
        trainer.set_params(params)

    trainer.train(model_name)

    return model_name

