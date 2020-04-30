#!usr/bin/python2.7
# coding=utf-8

#######################################################
# Name           : Multi BF (MBF) <cookie method>     #
# File           : main.py                            #
# Author         : DulLah                             #
# Recoder        : SkyMatz                            #
# Github         : https://github.com/skymatz         #
# Facebook       : https://www.facebook.com/dulahz    #
# Telegram       : https://t.me/unikers               #
# Python version : 2.7                                #
#######################################################

import os, time
from app import config
from app import login
from app import crack
from src import friends_list
from src import friends
from src import search_name
from src import likes
from bs4 import BeautifulSoup as parser

class Brute(object):
	def __init__(self, url):
		self.url = url
		self.config = config.Config()
		self.cookie = self.config.loadCookie()
		self.menu = '\n'
		self.menu = '\n'
		self.menu += '  01. Dump ID Temen\n'
		self.menu += '  02. Dump ID Cari nama\n'
		self.menu += '  03. Dump ID Dari like status\n'
		self.menu += '  04. Mulai Crack\n'
		self.menu += '  99. Hapus cookies\n'
		if self.cookie == False:
			login.loginFb(self, self.url, self.config)
			self.cookie = self.config.loadCookie()

	def start(self):
		response = self.config.httpRequest(self.url+'/profile.php', self.cookie).encode('utf-8')
		if 'mbasic_logout_button' in str(response):
			self.main(response)
		else:
			os.remove('log/cookies.log')
			print('\n\033[0;91m[•] Cookies tidak valid, coba lagi.\033[0m')
			raw_input('\n[ Press Enter]')
			login.loginFb(self, self.url, self.config)
			self.cookie = self.config.loadCookie()
			self.start()
			exit()

	def main(self, response):
		os.system('clear')
		print(self.config.banner())
		html = parser(response, 'html.parser')
		print('\n Pengguna Aktif : '.decode('utf-8')+html.title.text.upper())
		print(self.menu)
		try:
			choose = int(raw_input(' Pilih Angka : '))
		except ValueError:
			exit('\n\033[0;91mPake angka coek;v\033[0m')
		if choose == 199:
			exit(friends_list.main(self, self.cookie, self.url, self.config))
		elif choose == 1:
			exit(friends.main(self, self.cookie, self.url, self.config))
		elif choose == 2:
			exit(search_name.main(self, self.cookie, self.url, self.config))
		elif choose == 3:
			exit(likes.main(self, self.cookie, self.url, self.config))
		elif choose == 4:
			exit(crack.Brute().main())
		elif choose == 99:
			ask = raw_input('\nYakin lu coek? [y/n]: ')
			if ask.lower() == 'y':
				print('\nMenghapus cookies...')
				time.sleep(2)
				os.remove('log/cookies.log')
				print('\n\033[0;92mBerhasil dihapus ea;v\033[0m')
				time.sleep(2)
				login.loginFb(self, self.url, self.config)
				self.cookie = self.config.loadCookie()
				self.start()
			else:
				self.cookie = self.config.loadCookie()
				print('\nbatal;v!')
				self.start()
		else: exit('\n\033[0;91mLiat list gblk;v\033[0m')
