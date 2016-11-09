import attr2par
import par2vec

def getVec(attrs):
	par = attr2par.getPar(attrs)
	vec = par2vec.getVec(par)
	return vec
