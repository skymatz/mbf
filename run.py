#!usr/bin/python2.7
# coding=utf-8

#######################################################
# Name           : Multi BF (MBF) <cookie method>     #
# File           : run.py                             #
# Author         : DulLah                             #
# Recoder        : Skymatz                            #
# Github         : https://github.com/skymatz         #
# Facebook       : https://www.facebook.com/amtpages  #
# Telegram       : https://t.me/                      #
# Python version : 2.7                                #
#######################################################

import os, sys, shutil
from app import main as app

base_url = 'https://mbasic.facebook.com'

if sys.version_info.major != 2:
	sys.exit('\n\033[0;91m[*] Gunakan python versi 2\033[0m')

try: shutil.rmtree('app/__pycache__')
except: pass
try: shutil.rmtree('src/__pycache__')
except: pass

for filename in os.listdir('app'):
	if filename[-3:] == 'pyc':
		try: os.remove('app/'+filename)
		except: pass

for filename in os.listdir('src'):
	if filename[-3:] == 'pyc':
		try: os.remove('src/'+filename)
		except: pass

coekxd = app.Brute(base_url)
coekxd.start()

#end
