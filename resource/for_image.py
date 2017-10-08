#!/usr/bin/env python
#-*- coding:UTF-8 -*-

import os

path='/home/tla001/myworks/zrworks/mykk/resource/iceskater1'
f=open("images1.txt",'w')

files = list()
for pic in os.listdir(path):
	if(pic.find('.jpg')!=-1):
		files.append(pic)
files.sort()
for pic in files:
	f.write(os.path.join(path,pic)+'\n')

f.close()
