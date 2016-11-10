# -*- coding: utf-8 -*-



import numpy as np
from gensim.models.doc2vec import Doc2Vec 
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

def getPar2VecModel():
	# Loading of trained model ( Wikipedia ), to be charged one time 
	model_doc2vec = Doc2Vec.load('KB/enwiki_dbow/doc2vec.bin')
	stopwds = stopwords.words('english')
	return(stopwds, model_doc2vec)

def getVec(paragraph,stopwds,model_doc2vec):
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
    res_inter_stop = [w for w in res_inter if w not in stopwds]
    vect = model_doc2vec.infer_vector(res_inter_stop)
    return vect

if __name__=='__main__':
	print("Loading model...")
	(stopwds, model_doc2vec) = getPar2VecModel()
	print("Model loaded")
	par = 'I like to commit on git !'
	vec = getVec(par, stopwds, model_doc2vec)
	print(vec)
