#!usr/bin/python2.7
# coding=utf-8

#######################################################
# Name           : Multi BF (MBF) <cookie method>     #
# File           : search_name.py                     #
# Author         : DulLah                             #
# Recoder        : SkyMatz                            #
# Github         : https://github.com/skymatz         #
# Facebook       : https://www.facebook.com/dulahz    #
# Telegram       : https://t.me/unikers               #
# Python version : 2.7                                #
#######################################################

import os, re, sys, json
from bs4 import BeautifulSoup as parser
from datetime import datetime

def main(self, cookie, url, config):
	ask = raw_input('\nNama permintaan : ')
	if ask.strip() == '':
		exit("\n\033[0;91mWajib, tidak boleh kosong.\033[0m")
	try:
		max = int(raw_input('Mw nyari berapakh? (ex: 500): '))
	except ValueError:
		exit("\n\033[0;91mGblk;v\033[0m")
	if max == 0:
		exit("\n\033[0;91mWajib, tidak boleh kosong\033[0m")

	url_search = url+'/search/people/?q='+ask

	statusStop = False
	output = 'dump/'+ask.replace(' ', '_')+'.json'.strip()
	id = []
	print('')

	while True:
		try:
			response = config.httpRequest(url_search, cookie).encode('utf-8')
			html = parser(response, 'html.parser')
			find = html.find_all('a')
			for i in find:
				name = i.find('div')
				if '+' in str(name) or name == None:
					continue
				else:
					full_name = str(name.text.encode('utf-8'))
					if 'profile.php?id=' in str(i):
						uid = re.findall(r'\?id=(.*?)&', str(i))
					else:
						uid = re.findall('/(.*?)\?refid=', str(i))
					if len(uid) == 1:
						id.append({'uid': uid[0], 'name': full_name})
					sys.stdout.write("\r • %s                                        \r\n[\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m]"%(
						full_name, datetime.now().strftime('%H:%M:%S'), len(id)
					)); sys.stdout.flush()
					if len(id) == max or len(id) > max:
						statusStop = True
						break
			if statusStop == False:
				if 'Lihat Hasil Selanjutnya' in str(html):
					url_search = html.find('a', string='Lihat Hasil Selanjutnya')['href']
				else: break
			else: break
		except KeyboardInterrupt:
			print('\n\n\033[0;91mKeyInterrupt, stopped!!\033[0m')
			break
	try:
		for filename in os.listdir('dump'):
			os.remove('dump/'+filename)
	except: pass
	print('\n\nOutput: '+output)
	save = open(output, 'w')
	save.write(json.dumps(id))
	save.close()
