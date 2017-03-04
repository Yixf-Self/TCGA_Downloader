# -*- coding: utf-8 -*-
# @Author: rumia
# @Date:   2017-01-05 18:45:22
# @Last Modified by:   rumia
# @Last Modified time: 2017-01-05 19:37:48

import os, sys
import shutil

def assignFile(dict_fn_stage):
	for fn in dict_fn_stage:
		stage = dict_fn_stage[fn]
		stage_dn = stage.replace(' ', '_')
		try:
			os.mkdir(stage_dn)
		except:
			pass
		shutil.move(fn, stage_dn)
		print "[+] File '%s' has been assigned to '%s'" %(fn, stage_dn)
	print '[+] All files has been assigned to a certain stage directory.'
