from VCAP import example_image_embedding
from VGG16 import vgg16
from KB import attr2vec
from KB import par2vec
import numpy as np

def getVimage(imagePath):
	print("Calculating Vimage of "+imagePath)
	vcap = example_image_embedding.getVcap(imagePath)
	vattr, attrs = vgg16.getVattrAttr(imagePath)

	(stopwds, model_doc2vec) = par2vec.getPar2VecModel()
	vkb = attr2vec.getVec(attrs, stopwds, model_doc2vec)
	vimage = np.concatenate((vcap,vattr,vkb),axis=0)
	return vimage

if __name__=='__main__':
	vimage = getVimage('Data/train2014/COCO_train2014_000000487025.jpg')
	print(vimage)
	print(vimage.shape)
	
	
	

