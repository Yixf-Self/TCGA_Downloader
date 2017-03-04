# -*- coding: utf-8 -*-
# @Author: rumia
# @Date:   2017-01-05 17:46:27
# @Last Modified by:   rumia
# @Last Modified time: 2017-01-05 19:07:37

import requests
import StringIO
import json

def getStageForOneCase(case_id):
	pre = 'https://gdc-api.nci.nih.gov/cases/'
	suf = '?pretty=true&expand=diagnoses'
	url = pre + case_id + suf
	r = requests.get(url)
	try:
		handle = StringIO.StringIO(r.content)
		pretty = json.load(handle)
		return pretty['data']['diagnoses'][0]['tumor_stage']
	except Exception, error:
		print '[-]', error


def buildCaseStageMap(fn):
	"""
	fn: a json file downloaded from TCGA, which
	containing case_id, file_id, filename etc.
	"""
	fs_i = open(fn, 'rb')
	list_i = json.load(fs_i)
	raw_list = [d['cases'][0]['case_id'] for d in list_i]
	cid_list = list(set(raw_list))
	dict_case_stage = dict()
	count = 0
	l = len(cid_list)
	for case_id in cid_list:
		stage = getStageForOneCase(case_id)
		dict_case_stage.update({case_id: stage})
		count += 1
		print "[+] Get '%s' for %s (%d/%d)" %(stage, case_id, count, l)
	print '[+] Build Case-Stage Map: done.'
	return dict_case_stage


#print getStageForOneCase('0004d251-3f70-4395-b175-c94c2f5b1b81')

#buildCaseStageMap('files.json')
