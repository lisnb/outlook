#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2014-09-04 09:09:54
# @Last Modified by:   LiSnB
# @Last Modified time: 2014-12-30 14:38:21
# @Email: lisnb.h@gmail.com

"""
# @comment here:

"""

import datetime
import sys
import shutil
import platform
import os


def merge(src,static='./static',backup=True):
	timestamp = datetime.datetime.now().strftime('%m-%d')
	#host = './hosts-%s-%s'%(src,timestamp)
	host = src
	with open (host,'rb') as f:
		phosts = f.read()
	with open (static,'rb') as f:
		shosts = f.read()
	with open ('./hosts','wb') as f:
		f.write(shosts)
		f.write(phosts)
	hostfile = '/etc/hosts' if platform.system() == 'darwin' else 'C:\\Windows\\System32\\drivers\\etc\\hosts'
	if backup:
		shutil.copy(hostfile,hostfile+'-'+timestamp)
	shutil.copy('./hosts',hostfile)



if __name__ == '__main__':
	if len(sys.argv) < 2:
		print 'no src'
		exit()
	src = sys.argv[1]
	merge(src)
	







	