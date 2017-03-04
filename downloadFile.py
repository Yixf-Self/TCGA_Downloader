# -*- coding: utf-8 -*-
# @Author: rumia
# @Date:   2016-12-22 15:27:59
# @Last Modified by:   rumia
# @Last Modified time: 2017-01-05 18:39:09

import requests

def downloadByUUID(uuid):
	url = 'https://gdc-api.nci.nih.gov/data/' + uuid
	r = requests.get(url)
	filename = r.headers['Content-Disposition'].split('=')[-1]
	with open(filename, 'wb') as fd:
		for chunk in r.iter_content(chunk_size=128):
			fd.write(chunk)
	return filename

def downloadAll(list_fid):
	count = 0
	l = len(list_fid)
	for fid in list_fid:
		fn = downloadByUUID(fid)
		count += 1
		print "[+] Downloaded '%s' (%d/%d)" %(fn, count, l)
	print '[+] Download all files: done.'
