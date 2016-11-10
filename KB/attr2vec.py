import attr2par
import par2vec

def getVec(attrs, stopwds, model):
	par = attr2par.getPar(attrs)
	vec = par2vec.getVec(par, stopwds, model)
	return vec
