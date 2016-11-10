from VGG16 import vgg16
from KB import attr2vec

if __name__ == '__main__':
	vattr, attrs = vgg16.getVattrAttr('Data/dog.jpg')
	vec = attr2vec.getVec(attrs)
	print("******\n")
	print(vec)

