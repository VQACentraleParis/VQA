from VCAP import example_image_embedding
from VGG16 import vgg16
from KB import attr2vec
import numpy as np

def getVimage(imagePath):
	vcap = example_image_embedding.getVcap(imagePath)
	vattr, attrs = vgg16.getVattrAttr(imagePath)
	vkb = attr2vec.getVec(attrs)
	vimage = np.concatenate((vcap,vattr,vkb),axis=0)
	return vimage

if __name__=='__main__':
	vimage = getVimage('Data/cat.jpg')
	print(vimage)
	
	
	

