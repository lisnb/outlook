#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LiSnB
# @Date:   2014-09-04 09:09:54
# @Last Modified by:   LiSnB
# @Last Modified time: 2014-09-04 09:21:44
# @Email: lisnb.h@gmail.com

"""
# @comment here:

"""

import datetime


def merge(static='./static'):
	projecth = './hosts-project-h-'+datetime.datetime.now().strftime('%m-%d')
	with open (projecth,'rb') as f:
		phosts = f.read()
	with open (static,'rb') as f:
		shosts = f.read()
	with open ('./hosts','wb') as f:
		f.write(shosts)
		f.write(phosts)





if __name__ == '__main__':
	merge()
	







	