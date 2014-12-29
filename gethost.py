#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2014-09-04 09:09:54
# @Last Modified by:   LiSnB
# @Last Modified time: 2014-12-29 16:39:29
# @Email: lisnb.h@gmail.com

"""
# @comment here:

"""

import datetime
import sys
import shutil


def merge(src,static='./static'):
	timestamp = datetime.datetime.now().strftime('%m-%d')
	host = './hosts-%s-%s'%(src,timestamp)
	with open (host,'rb') as f:
		phosts = f.read()
	with open (static,'rb') as f:
		shosts = f.read()
	with open ('./hosts','wb') as f:
		f.write(shosts)
		f.write(phosts)
	shutil.copy('C:\\Windows\\System32\\drivers\\etc\\hosts','C:\\Windows\\System32\\drivers\\etc\\hosts-%s'%timestamp)
	shutil.copy('./hosts','C:\\Windows\\System32\\drivers\\etc\\hosts')





if __name__ == '__main__':
	if len(sys.argv) < 2:
		print 'no src'
		exit()
	src = sys.argv[1]
	merge(src)
	







	