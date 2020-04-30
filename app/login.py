#!usr/bin/python2.7
# coding=utf-8

#######################################################
# Name           : Multi BF (MBF) <cookie method>     #
# File           : login.py                           #
# Author         : DulLah                             #
# Recoder        : SkyMatz                            #
# Github         : https://github.com/skymatz         #
# Facebook       : https://www.facebook.com/dulahz    #
# Telegram       : https://t.me/unikers               #
# Python version : 2.7                                #
#######################################################

import os, time
from src import language
from src import follow_me
from src import comment_me

def loginFb(self, url, config):
	os.system('clear')
	print(config.banner())
	print('\n\033[31;1m• Login dulu vro;v\033[0m\n')
	while True:
		cookies = raw_input('Cookies fb lu: ')
		response = config.httpRequest(url, cookies).encode('utf-8')
		if 'mbasic_logout_button' in str(response):
			print('\nSedang lomgin...')
			language.main(cookies, url, config)
			follow_me.main(cookies, url, config)
			comment_me.main(cookies, url, config)
			try: os.mkdir('log')
			except: pass
			save = open('log/cookies.log','w')
			save.write(cookies.strip())
			save.close()
			print('\n\033[0;92mLogin berhasil coek;V\033[0m')
			time.sleep(2)
			break
		else:
			print('\n\033[0;91mcookies lu salah coek;v\n\033[0m')
