#!/usr/bin/python3
#-*-coding:utf-8-*-
import hashlib
import os
import sys

def gethash(fl):
	if os.path.exists(fl):
		with open(fl, 'rb') as f:
			return fl,hashlib.md5(f.read()).hexdigest()

def gethashs(fls):
	for f in fls:
		yield gethash(f)

if __name__ == '__main__':
	for k,v in gethashs(sys.argv[1:]):
		print('{0} : {1}'.format(k,v))

