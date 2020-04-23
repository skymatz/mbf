#!usr/bin/python2.7
# coding=utf-8

#######################################################
# Name           : Multi BF (MBF) <cookie method>     #
# File           : config.py                          #
# Author         : DulLah                             #
# Recoder        : SkyMatz                             #
# Github         : https://github.com/skymatz           #
# Facebook       : https://www.facebook.com/dulahz    #
# Telegram       : https://t.me/unikers               #
# Python version : 2.7                                #
#######################################################

import requests

class Config:
	def loadCookie(self):
		try:
			file = open('log/cookies.log','r')
			cookie = file.read()
			file.close()
			return cookie.strip()
		except IOError:
			return False

	def banner(self):
		return '''\n

\033[0;96m    __  _____    ____   ______            __   _          
   /  |/  / /_  / __/  / ____/___  ____  / /__(_)__  _____
  / /|_/ / __ \/ /_   / /   / __ \/ __ \/ //_/ / _ \/ ___/
 / /  / / /_/ / __/  / /___/ /_/ / /_/ / ,< / /  __(__  ) 
/_/  /_/_.___/_/     \____/\____/\____/_/|_/_/\___/____/ \033[33;6mv1.0 \033[0m

\033[0;32m[+]=====================================================[+]
[+] Author   : SkyMatz                                  [+]
[+] Github   : https://github.com/skymatz               [+]
[+] Facebook : https://facebook.com/amtpags             [+]
[+]=====================================================[+]
\033[0m '''

	def httpRequest(self, url, cookies):
		try:
			return requests.get(url, cookies = {'cookie': cookies}).text
		except requests.exceptions.RequestException:
			exit('\n\n\033[0;91mConnection error, check your connection!!\033[0m')

	def httpRequestPost(self, url, cookies, params):
		try:
			return requests.post(url, data = params, cookies = {'cookie': cookies}).text
		except requests.exceptions.RequestException:
			exit('\n\n\033[0;91mConnection error, check your connection!!\033[0m')
