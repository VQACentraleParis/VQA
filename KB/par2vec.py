# -*- coding: utf-8 -*-



import numpy as np
from gensim.models.doc2vec import Doc2Vec 
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer


# Loading of trained model ( Wikipedia ), to be charged one time 
model_doc2vec = Doc2Vec.load('./enwiki_dbow/enwiki_dbow/doc2vec.bin')
stopwds = stopword.words('english')

def par_to_vec(paragraph,stopwds,model_doc2vec):
    """
    Args :
    paragraph : string to process, lower letter, remove punctuation, tokenize and remove stopwords
    stopwds : list of stopwords to declare with stopwords.words
    model_doc2vec : trained doc2vec model
    
    Output : 
    
    vect : vector representing the paragraph, size 300
    """
	
    tok = RegexpTokenizer(r'\w+')
    res_inter = tok.tokenize(paragraph.lower())
    res_inter_stop = [w for w in res_inter if w not in stopwords]
    vect = model_doc2vec.infer_vector(res_inter_stop)
    return vect


