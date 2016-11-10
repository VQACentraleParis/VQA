import tensorflow as tf
import utils as ut
from scipy import misc
import image_embedding
from image_embedding import inception_v3


def getVcap(imagePath):
	cat = misc.imread(imagePath)
	cat = misc.imresize(cat,(299,299))

	batch_size = 1
	height = 299
	width = 299
	num_channels = 3
	batch = cat.reshape((1, 299, 299, 3))
	assert batch.shape == (1, 299, 299, 3)
	images = tf.placeholder(tf.float32,[batch_size, height, width, num_channels])
	model = inception_v3(images)
	saver = tf.train.Saver()

	with tf.Session() as sess:
	  init = tf.initialize_all_variables()
	  sess.run(init)
	  #print "variables initialized"
	  saver.restore(sess, "VCAP/inception_v3.ckpt")
	  #print("Model restored.")

	  

	  feed_dict = { images: batch }

	  result = sess.run(model, feed_dict=feed_dict)
	print("Vcap calculated")
        return result[0,:]

if __name__=='main':
	#cat = utils.load_image("cat.jpg")
	cat = misc.imread("Data/dog.jpg")
	cat = misc.imresize(cat,(299,299))

	batch_size = 1
	height = 299
	width = 299
	num_channels = 3
	batch = cat.reshape((1, 299, 299, 3))
	assert batch.shape == (1, 299, 299, 3)
	images = tf.placeholder(tf.float32,[batch_size, height, width, num_channels])
	model = inception_v3(images)
	saver = tf.train.Saver()

	with tf.Session() as sess:
	  init = tf.initialize_all_variables()
	  sess.run(init)
	  print "variables initialized"
	  saver.restore(sess, "inception_v3.ckpt")
	  print("Model restored.")

	  

	  feed_dict = { images: batch }

	  result = sess.run(model, feed_dict=feed_dict)

	print("*******************\n")
	print(result[0,:].shape)
	print("*******************\n")
	print(type(result))
	print("*******************\n")
	print(result[0,:])


