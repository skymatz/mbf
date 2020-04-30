#!usr/bin/python2.7
# coding=utf-8

#######################################################
# Name           : Multi BF (MBF) <cookie method>     #
# File           : config.py                          #
# Author         : DulLah                             #
# Recoder        : SkyMatz                            #
# Github         : https://github.com/skymatz         #
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
    }--------------------------------------{
}-----> Multi Brute Force Cookies Method <-----{
    }--------------------------------------{
    
 • coded ./skymatz             • fb.me/amttidz
 • github.com/skymatz          • version 1.0
'''
	def httpRequest(self, url, cookies):
		try:
			return requests.get(url, cookies = {'cookie': cookies}).text
		except requests.exceptions.RequestException:
			exit('\n\n\033[0;91mKoneksi error coek;v\033[0m')

	def httpRequestPost(self, url, cookies, params):
		try:
			return requests.post(url, data = params, cookies = {'cookie': cookies}).text
		except requests.exceptions.RequestException:
			exit('\n\n\033[0;91mKoneksi error coek;v\033[0m')
