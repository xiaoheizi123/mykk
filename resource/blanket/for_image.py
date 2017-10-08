#!/usr/bin/env python
#-*- coding:UTF-8 -*-

import os

path='/home/zr/documents/KCFcpp/resource/blanket'
f=open("images.txt",'w')

for pic in os.listdir(path):
	f.write(os.path.join(path,pic)+'\n')

f.close()
