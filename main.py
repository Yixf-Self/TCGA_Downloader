# -*- coding: utf-8 -*-
# @Author: rumia
# @Date:   2017-01-05 18:59:26
# @Last Modified by:   rumia
# @Last Modified time: 2017-01-05 19:43:17

from buildCaseStageMap import buildCaseStageMap
from buildFileCaseMap import buildFileCaseMap
from downloadFile import downloadAll
from unzipFile import unzipAll, removeZippedFile
from assignFile import assignFile

def buildAll(json_fn):
	"""
	json_fn: a json file downloaded from TCGA, which
	containing case_id, file_id, filename etc.
	"""
	dict_case_stage = buildCaseStageMap(json_fn)
	dict_fn_case, list_fid = buildFileCaseMap(json_fn)
	dict_fn_stage = {fn: dict_case_stage[dict_fn_case[fn]] for fn in dict_fn_case}
	downloadAll(list_fid)
	unzipAll()
	removeZippedFile()
	assignFile(dict_fn_stage)

buildAll('files.json')


