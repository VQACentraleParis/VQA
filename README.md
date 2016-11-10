# VQA


## Installation

You need to first download the model "inception_v3.cpkt" as such in VCAP directory :

```powerconsole
cd VCAP/
wget "http://download.tensorflow.org/models/inception_v3_2016_08_28.tar.gz"
tar -xvf "inception_v3_2016_08_28.tar.gz"
rm "inception_v3_2016_08_28.tar.gz"
```

You need to download the weights "vgg16_weights.npz" in VGG16 directory, that you can find on this website :
http://www.cs.toronto.edu/~frossard/post/vgg16/

Aftward to get the program running, the easiest and more clean way is to create a virtualenv

```
$ pip install virtualenv
```

Afterward you will create a clean virtualenv for the VQA

```
$ virtualenv vqaenv
```

To begin using the virtual environment, it needs to be activated:

```
$ source vqaenv/bin/activate
```

If it is the first time you will need to install the required packages with proper version that will not conflict with python env
```
$ pip install -r requirements.txt
```


Also you will need to install gensim
```
$ pip install --upgrade gensim
```

If you are done working in the virtual environment for the moment, you can deactivate it:

```
$ deactivate
```
