from VGG16 import vgg16

if __name__ == '__main__':
	vattr, attrs = vgg16.getVattrAttr('VGG16/laska.png')
	print(vattr)
        print("************\n")
        print(attrs)
