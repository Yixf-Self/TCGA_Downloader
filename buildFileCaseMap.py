# -*- coding: utf-8 -*-
# @Author: rumia
# @Date:   2017-01-05 18:20:12
# @Last Modified by:   rumia
# @Last Modified time: 2017-01-05 19:42:34

import json

def buildFileCaseMap(fn):
	"""
	fn: a json file downloaded from TCGA, which
	containing case_id, file_id, filename etc.
	"""
	fs_i = open(fn, 'rb')
	list_i = json.load(fs_i)
	dict_fn_case = dict()
	list_fid = list()
	for d in list_i:
		if d['file_name'].endswith('FPKM-UQ.txt.gz'):
			dict_fn_case.update({d['file_name'][:-3]: d['cases'][0]['case_id']})
			list_fid.append(d['file_id'])
	return dict_fn_case, list_fid

#dict_fn_case, list_fid = buildFileCaseMap('files_large.json')
#print len(list_fid)
