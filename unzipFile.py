# -*- coding: utf-8 -*-
# @Author: rumia
# @Date:   2016-12-22 15:38:44
# @Last Modified by:   rumia
# @Last Modified time: 2017-01-05 19:37:12

import os, sys
import gzip

def unzip(zipped_file):
	fs_i = gzip.open(zipped_file, 'rb')
	fn = zipped_file[:-3]
	fs_o = open(fn, 'w+')
	text = fs_i.read()
	fs_o.write(text)
	fs_i.close()
	fs_o.close()
	return None

def unzipAll():
	lst = os.listdir('./')
	lst_ = list(filter(lambda x: x.endswith('FPKM-UQ.txt.gz'), lst))
	count = 0
	l = len(lst_)
	for f in lst_:
		unzip(f)
		count += 1
		print "[+] Unzip file '%s' successfully (%d/%d)" %(f, count, l)
	print '[+] Unzip all files: done.'

def removeZippedFile():
	lst = os.listdir('./')
	lst_ = list(filter(lambda x: x.endswith('FPKM-UQ.txt.gz'), lst))
	for f in lst_:
		os.remove(f)
		print "[+] Remove file '%s': done." %(f)
	print '[+] Successfully removed all zipped file.'
