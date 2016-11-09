from VGG16 import vgg16
from KB import attr2par

if __name__ == '__main__':
	vattr, attrs = vgg16.getVattrAttr('Data/dog.jpg')
	par = attr2par.getPar(attrs)
	print("******\n")
	print(par)

