# -*- coding: utf-8 -*-

from KB import dbpedia_request
from VGG16 import vgg16


def getPar(attrs):
	par = ''
	visited = []
	for attr in attrs:
		if len(attr.split(' '))>1:
			for word in attr.split(' '):
				word = word.title()
				if word not in visited :
					par+=' '+dbpedia_request.get_description(word)
					visited.append(word)
		else:
			attr=attr.title()
			if attr not in visited:
				par+=' '+dbpedia_request.get_description(attr)
				visited.append(attr)
	return par

