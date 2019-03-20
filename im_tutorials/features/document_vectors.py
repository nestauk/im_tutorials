import numpy as np


def document_vector(word2vec_model, doc):
    # remove out-of-vocabulary words
    doc = [word for word in doc if word in word2vec_model.wv.vocab]
    if doc:
        return np.mean(word2vec_model[doc], axis=0)
    else:
        return np.zeros(word2vec_model.trainables.layer1_size,)
