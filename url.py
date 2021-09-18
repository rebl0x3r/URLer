#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''

							+-----------------------------------------+
							|                                         |
							|  PROJECT     : URLer                    |
							|  DESCRIPTION : Scampage URL Kit         |
							|  RELEASE     : V1                       |
							|  AUTHOR      : @F4C3R100                |
							|  CREATION    : 2021-08-02               |
							|                                         |
							+-----------------------------------------+
							|                                         |
							|  TODO:                                  |
							|  ----                                   |
							|  |- add more combinations               |
							|  |- add more shorteners (shortlinks)    |
							|  |____________________________________  |
							|                                         |
							+-----------------------------------------+



												'''

# Settings

'''
	
	0 means disabled (Boolean)
	1 means enabled (Boolean)

	Values higher than one are integers(numbers). Max count for example could be 10, 20 etc.

	String Settings can be written as you want, for example you can change directory name or file path.

''' 

''' Boolean Settings '''

all_strings	= 1		# Generate Uppercase, Lowercase, Digits -, _ and .
check_count	= 0		# Check max_count On 'random_strings' Function
digits		= 1		# Generate Digits
enable_www	= 1		# Add www(.) To URL
enable_ddns	= 1		# Add (.)ddns.net To URL
save_urls	= 1		# Save Generated URLs Into An Extra File
save_words	= 1		# Save Generated Words Into An Extra File 
uniq_random	= 0		# Remove Duplicates From A Randomized String (1 Means The String Is Shorter Than The Length)
use_https	= 1		# Use HTTPS (if 0 then http)
use_trick	= 1		# Use Trick To Trick Google Safebrowsing(Swap First And Last URL Letter)
remove_quote = 1	# Remove Quotes: ' And " From URLs

''' Integer Settings '''
bl_count	= 1		# Max Length Of Changing Letter To Number (ex: 1 is p4pal, 2 is p4yp4l) 
max_count	= 10 	# Max Length Of Random Generated String

''' String Settings ''' 

words_file 	= 'words.txt' 	# Output File (Words)
output_file	= 'urls.txt'	# Output File (URL)
path		= 'result'		# Output Path (Results)
leet_mode 	= 'normal'		# Leetmode (normal = a,e,i,o,u | extreme = normal, s,t,u)


# Variables (DON'T CHANGE)

version		= 1
username	= ''
platform	= ''
keywords 	= ['api', 'bound', 'connect', 'content', 'defend', 'fast', 'j_secure', 'local', 'oauth', 'oth', 'protect', 'root', 'safe', 'secure', 'server', 'service', 'session', 'stable', 'support', 'system', 'trusted']
special_chars = ['','_','','-','','.']
banner = f"""	      \033[94m_   _ ____  _              \n	     \033[94m|\033[42m \033[0;94m| |\033[42m \033[0;94m|  _ \\| | \033[92;1;41m@f4c3r100\033[0;94m__ \n	     \033[94m|\033[42m \033[0;94m| |\033[42m \033[0;94m| |_) | |   / _ \\ '__|\n	     \033[94m|\033[42m \033[0;94m|_|\033[42m \033[0;94m|  _ <| |__|  __/ | \033[33;1mv\0{version}\033[0;94m  \n	      \033[94m\\\033[42m___\033[0;94m/|_| \\_\\_____\\___|_|   \n                             \n\033[31;1m               (  .      )\n           )           (              )\n                 .  '   .   '  .  '  .\n        (    , )       (.   )  (   ',    )\n         .' ) ( . )    ,  ( ,     )   ( .\n      ). , ( .   (  ) ( , ')  .' (  ,    )\n     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )\n    \033[30m^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n    G E N E R A T E  P H I S H I N G  U R L S\n\033[0m\n    \t\t\033[31;1mIssues? \033[37mReport Them:\n\033[0m\n    \033[34;1mGitHub   : \033[32mhttps://github.com/rebl0x3r/URLer/issues\n    \033[34;1mTelegram : \033[32mhttps://t.me/f4c3r100\033[0m\n\n"""
byebye = """	THANKS\n	FOR\n	USING\n	THIS\n	TOOL\n	@f4c3r100 :)\n"""


# Import Modules

try:
	import faker, getpass, os, random, string, sys, re, requests, random_word, json
except:
	print(f"Module Not Installed[\033[32mFixer\033[37m]")
	print(f"Trying to fix.... [\033[32mFixer\033[37m]")
	try:
		import sys,os
		if sys.platform == 'linux' or sys.platform == 'darwin':
			print(f"Installing requirements.... [\033[32mFixer\033[37m]")
			os.system('python3 -m pip install requirements.txt')
			print(f"Installed, please run again the tool [\033[32mFixer\033[37m]")

		if sys.platform == 'win32':
			print(f"Installing requirements.... [\033[32mFixer\033[37m]")
			os.system('py -m pip install requirements.txt')
			print(f"Installed, please run again the tool [\033[32mFixer\033[37m]")
	except:
		print(f"Unknown Error, Contact @f4c3r100 [\033[32mFixer\033[37m]")
		sys.exit(1)

	sys.exit(1)

# System Functions

def clear(plat):
	# Print Version :

	''' print('\x1b[2J') '''

	# OS Version :
	
	if plat == 'Linux' or plat == 'MacOS':
		os.system('clear')
	if plat == 'Windows':
		os.system('cls')

def dependencies_check():
	global error
	global path
	global username
	global hostname
	global platform 

	try:
		if sys.platform == 'linux':
			platform = 'Linux'
		elif sys.platform == 'win32':
			platform = 'Windows'
		elif sys.platform == 'darwin':
			platform = 'MacOS'
		else:
			error = 'Unknown Platform'
	except:
		error = 'Unknown Error (Dependencies[\033[32mPlatform\033[37m])'
		return False

	try:
		hostname = os.uname().nodename
	except:
		hostname = 'scarletta'

	try:
		username = getpass.getuser()
	except:
		username = 'f4c3r100'
		
	try:
		if not os.path.isdir(path):
			os.makedirs(path)
	except:
		error = f"Can't Create Directory(Directory[\033[32m{path}\033[37m])"
		return False

	try:
		if not os.path.exists(path+"/"+output_file):
			open(path+"/"+output_file, 'a').close()
	except:
		error = f"Can't Create File(File[\033[32m{output_file}\033[37m])"
		return False

	return True


def saver(filename, content):
	temp = open(filename, "a")
	temp.write(content)
	temp.close()


# Tool Functions

def string_reverse(word):
	return word[::-1]

def swap_chars(word):
	s = word[0]
	l = word[-1]
	return l + word[1:-1] + s

def randomize(word):
	global uniq_random
	wordlist 	= []
	randomized 	= []
	number 		= 0

	for _ in word:
		wordlist.append(_)

	while number < len(wordlist):
		randomized.append(wordlist[random.randint(0,len(wordlist)-1)])
		if uniq_random:

			''' 
				
			NOTE : The following code removes duplicates, the issue is that you will get a less length than the orignal input string.

			'''

			randomized = list(dict.fromkeys(randomized))
		number += 1

	final = ''.join(randomized)

	return final


def random_strings(count):
	global digits
	global max_count
	global check_count
	global all_strings

	if check_count:
		if int(count) > int(max_count):
			print(f"\033[34m[\033[31;1m!\033[0;34m] \033[37mThe max number of random string is reached\033[34m(\033[32;1m{max_count}\033[0;34m)\033[37m. Please change the value on line \033[31m54 \033[37mfor a higher randomized max count.\033[0m")
			count = 7
			return False
	if all_strings:
		chars = string.ascii_lowercase + string.ascii_uppercase + "_-."

	if digits:
		chars += string.digits

#	count = int(count) + 1
	return ''.join(random.choice(chars) for _ in range(1, int(count) + 1))

def leetmode(chars):
	'''abcdefghijklmnopqrstuvwxyz'''
	global bl_count
	global leet_mode
	if leet_mode == 'normal':
		leetmode = {'a': '4','e': '3','i': '1','o': '0','u': 'v'}
	elif leet_mode == 'extreme':
		leetmode = {'a': '4','e': '3','i': '1','o': '0','u': 'v','s': '5','t': '7', 'v': 'u'}
	blacklist = {}
	
	for char in chars:
		if char.isupper():
			char = char.lower()
		if leetmode.get(str(char)):
			if blacklist.get(str(char)):
				if int(blacklist.get(char)) < int(bl_count):
					chars = chars.replace(str(char), leetmode.get(str(char)), 1)
					blacklist.update(char = blacklist.get(char) + 1)
			else:
				chars = chars.replace(str(char), leetmode.get(str(char)), 1)
				blacklist[char] = 1


	return chars

def format_url(url):
	if "http://" or "https://" in url:
		url = re.sub("https?://", "", url)
	return url


def safebrowsing(url):
	url = format_url(url)
	response = requests.get('https://www.google.com/transparencyreport/api/v3/safebrowsing/status?site={}'.format(url), timeout=3).text
	if 'sb.ssr",6' in response or 'sb.ssr",4' in response or 'sb.ssr",1' in response:
		return 'live';
	elif 'sb.ssr",2' in response:
		return 'dead';
	else:
		return False


def generate_words(count):
	global path
	global keywords
	global save_words
	global words_file

	counter = 0

	if int(count) == 1:
		try:
			temp_word = random_word.RandomWords().get_random_word()
			if temp_word == None or temp_word == 'None':
				return random_word.RandomWords().get_random_word().replace("'","")
			else:
				return temp_word
		except:
			return random.choice(keywords)
	else:
		for _ in range(0,int(count)):
			counter += 1
			word = random_word.RandomWords().get_random_word()
			print(f"\033[34m[\033[33;1m*\033[0;34m] \033[37mGenerated Word({counter}/{count}) : \033[33m{word}")
			if save_words:
				saver(f"{path}/{words_file}",f"{word}\n")


def generate_url(count):
	''' Intelligence URL Generator '''
	global path
	global keywords
	global save_urls
	global use_trick
	global enable_www
	global enable_ddns
	global output_file
	global remove_quote

	counter = 0 
	for _ in range(1, int(count)+1):
		counter += 1
		words = random.choice(keywords) + "-" + random.choice(keywords)
		if use_trick:
			words = swap_chars(words)
		words = leetmode(words)
		if enable_www:
			if not re.findall("^w{3}\.",words):
				words = 'www.' + words
			if not "https://" in words or not "http://" in words:
				if use_https:
					words = 'https://' + words
				else:
					words = 'http://' + words
		if enable_ddns:
			if re.findall("[.]{1}$", words):
				words = words + 'ddns.net'
			else:
				words = words + '.ddns.net'

		if remove_quote:
			words = words.replace("'","")
			words = words.replace('"','')

		if save_urls:
			saver(f"{path}/{output_file}", f"{words}\n")
		print(f"\033[34m[\033[33;1m*\033[0;34m] \033[37mGenerated URL: ({counter}/{count}) : \033[33m{words}")

	''' In Progress...'''

def m_url(count):
	''' Random Word + Swap + Leetmode + Random Chars '''
	global path
	global save_urls
	global enable_www
	global enable_ddns
	global output_file
	global remove_quote
	global special_chars 

	counter		= 0

	for _ in range(0, int(count)):
		superduper = ''
		counter += 1
		word = generate_words(1)
		swap = swap_chars(word)
		leet = leetmode(swap)
		random_number = random.randint(1,3)
		main = [leet[i:i+random_number] for i in range(0, len(leet), random_number)]
		for part in main:
			superduper += random.choice(special_chars) + part
		
		
#		print(superduper+'.ddns.net')
		if re.findall("^(_|-|\.)",superduper):
			superduper = superduper.replace(re.findall("^(_|-|\.)",superduper)[0], '')
		if enable_www:
			if not re.findall("^w{3}\.",superduper):
				superduper = 'www.' + superduper
			if not "https://" in superduper or not "http://" in superduper:
				if use_https:
					superduper = 'https://' + superduper
				else:
					superduper = 'http://' + superduper
		if enable_ddns:
			if re.findall("[.]{1}$", superduper):
				superduper = superduper + 'ddns.net'
			else:
				superduper = superduper + '.ddns.net'

		if remove_quote:
			superduper = superduper.replace("'","")
			superduper = superduper.replace('"','')	

		if save_urls:
			saver(f"{path}/{output_file}", f"{superduper}\n")

		print(f"\033[34m[\033[33;1m*\033[0;34m] \033[37mGenerated URL: ({counter}/{count}) : \033[33m{superduper}")

def s_url(count):
	''' Random Word + Randomize + String Rev + Leetmode '''
	global path
	global save_urls
	global output_file
	global remove_quote
	global special_chars 

	counter		= 0

	for _ in range(0, int(count)):
		superduper = ''
		counter += 1
		word = generate_words(1)
		rand = randomize(word.strip())
		strrev = string_reverse(rand)
		leet = leetmode(strrev)
		random_number = random.randint(1,3)
		main = [leet[i:i+random_number] for i in range(0, len(leet), random_number)]
		for part in main:
			superduper += random.choice(special_chars) + part
		
		
#		print(superduper+'.ddns.net')
		if re.findall("^(_|-|\.)",superduper):
			superduper = superduper.replace(re.findall("^(_|-|\.)",superduper)[0], '')
		if enable_www:
			if not re.findall("^w{3}\.",superduper):
				superduper = 'www.' + superduper
			if not "https://" in superduper or not "http://" in superduper:
				if use_https:
					superduper = 'https://' + superduper
				else:
					superduper = 'http://' + superduper
		if enable_ddns:
			if re.findall("[.]{1}$", superduper):
				superduper = superduper + 'ddns.net'
			else:
				superduper = superduper + '.ddns.net'
		
		if remove_quote:
			superduper = superduper.replace("'","")
			superduper = superduper.replace('"','')

		if save_urls:
			saver(f"{path}/{output_file}", f"{superduper}\n")

		print(f"\033[34m[\033[33;1m*\033[0;34m] \033[37mGenerated URL: ({counter}/{count}) : \033[33m{superduper}")

def l_url(count):
	''' Random String + String Reverse + Leetmode + Randomize '''
	global path
	global save_urls
	global max_count
	global output_file
	global remove_quote
	global special_chars 

	counter		= 0

	for _ in range(0, int(count)):
		superduper = ''
		counter += 1
		
		''' 
	
		You can also use the max_count value, but it's
		better to use here 12, because we can work better
		with the length of 12 characters than with custom
		length like 1,2,3. Make sure you disabled the 
		'check_count' to use the value of 12 or add them
		as 'max_count' value to the settings.


		'''
	
		#random_string = random_strings(max_count) 

		random_string = random_strings(12) 
		strrev = string_reverse(random_string)
		leet = leetmode(strrev)
		rand = randomize(leet.strip())

		random_number = random.randint(1,3)
		main = [rand[i:i+random_number] for i in range(0, len(rand), random_number)]
		for part in main:
			superduper += random.choice(special_chars) + part
		
		
#		print(superduper+'.ddns.net')
		if re.findall("^(_|-|\.)",superduper):
			superduper = superduper.replace(re.findall("^(_|-|\.)",superduper)[0], '')
		if enable_www:
			if not re.findall("^w{3}.",superduper):
				superduper = 'www.' + superduper
			if not "https://" in superduper or not "http://" in superduper:
				if use_https:
					superduper = 'https://' + superduper
				else:
					superduper = 'http://' + superduper
		if enable_ddns:
			if re.findall("[.]{1}$", superduper):
				superduper = superduper + 'ddns.net'
			else:
				superduper = superduper + '.ddns.net'
		if remove_quote:
			superduper = superduper.replace("'","")
			superduper = superduper.replace('"','')

		if save_urls:
			saver(f"{path}/{output_file}", f"{superduper.lower()}\n")

		print(f"\033[34m[\033[33;1m*\033[0;34m] \033[37mGenerated URL: ({counter}/{count}) : \033[33m{superduper.lower()}")

def short_url(url):
	URL_LIST = []
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.3538.77 Safari/537.36','Accept': '*/*','Accept-Language': 'en-US,en;q=0.5','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','X-Requested-With': 'XMLHttpRequest','Origin': 'http://gg.gg','DNT': '1','Connection': 'keep-alive','Referer': 'http://gg.gg/','Pragma': 'no-cache','Cache-Control': 'no-cache'}
	data = {'custom_path': '','use_norefs': '1','long_url': url,'app': 'site','version': '0.1'}
	response = requests.post('http://gg.gg/create', headers=headers, data=data)
	if response.status_code == 200:
		URL_LIST.append(response.text.replace('http','https'))
	else:
		return 'Invalid'

	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Language': 'en-US,en;q=0.5','Content-Type': 'application/x-www-form-urlencoded','Origin': 'https://www.shorturl.at','DNT': '1','Connection': 'keep-alive','Referer': 'https://www.shorturl.at/','Upgrade-Insecure-Requests': '1','Pragma': 'no-cache','Cache-Control': 'no-cache','TE': 'Trailers'}
	data = {'u': url}
	
	response = requests.post('https://www.shorturl.at/shortener.php', headers=headers, data=data)
	if re.findall('shorturl.at\/[a-zA-Z0-9]{1,6}', response.text):
		shorten = re.findall('shorturl.at\/[a-zA-Z0-9]{1,6}', response.text)
		url_ = list(dict.fromkeys(shorten))[0]
		if url_:
			URL_LIST.append('https://'+str(url_))
		else:
			return 'Invalid'

	cookies = {'XSRF-TOKEN': 'eyJpdiI6InlUU0FcL1ByM0ZYWFwvelFqclVJa3ZuUT09IiwidmFsdWUiOiJ6MVZ1VmRSUm5WVVU2UmcrMEdJZTN1bEtqc3JnTEZGSHVsV0U5NW1Lc0JwbWhzcGllV1JDdzZCVFRSSGgxaHBabkl0WlBcL21UNkxjK0twUjdOR3lTbXdQbitkcmVQRldnbXVOcEhBaUNQR3BiXC9tU3FxY2QxQ0g5WnJKT2UyU3NjIiwibWFjIjoiMGQ0OGYzZTMxOWZiNWU0MzU4NmQzNGYwOTFlZjQyMTRmY2U4ZDczYmZiZTdmODc2ODM4MWUzN2RhZWU1Y2JlZSJ9','tinyurl_session': 'eyJpdiI6IjE5VEhNZjJrZG14SUsrTlYxSFQrWXc9PSIsInZhbHVlIjoieTFrVHNBU0N0TjJrWTJPbkFkUmJZZk0zYXB3ZHVSZlJqOUF2R2FLb04rSDFYVGx3bm1WclhLbFZyWnBCSVVQakZFQk0zU2dMYm1Hd2s1dDZvbzhnT1Y2cjRGRXNyOUVFdVdxMEpYWCtBXC9sRFlcL3o0cHI1RjdCZXpPaWxZc1VUMSIsIm1hYyI6IjgwOTYyOThiNjczM2JmMzM1MjRjNDU2NTIyNjA5NDUxYzQ3MzA2ZTg2MjAwNDNlYzU3OWNkM2RmYmM3NDAzZDIifQ%3D%3D','tinyUUID': '13f80a238a34d16bc4c4000073de552b','early-access': 'yes%7C2021-09-13T16%3A47%3A24.232%2B00%3A00','tinyWULI': '1631553262'}

	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0','Accept': '*/*','Accept-Language': 'en-US,en;q=0.5','X-Requested-With': 'XMLHttpRequest','Content-Type': 'application/json;charset=utf-8','X-XSRF-TOKEN': 'eyJpdiI6InlUU0FcL1ByM0ZYWFwvelFqclVJa3ZuUT09IiwidmFsdWUiOiJ6MVZ1VmRSUm5WVVU2UmcrMEdJZTN1bEtqc3JnTEZGSHVsV0U5NW1Lc0JwbWhzcGllV1JDdzZCVFRSSGgxaHBabkl0WlBcL21UNkxjK0twUjdOR3lTbXdQbitkcmVQRldnbXVOcEhBaUNQR3BiXC9tU3FxY2QxQ0g5WnJKT2UyU3NjIiwibWFjIjoiMGQ0OGYzZTMxOWZiNWU0MzU4NmQzNGYwOTFlZjQyMTRmY2U4ZDczYmZiZTdmODc2ODM4MWUzN2RhZWU1Y2JlZSJ9','Origin': 'https://tinyurl.com','DNT': '1','Connection': 'keep-alive','Referer': 'https://tinyurl.com/app/','Pragma': 'no-cache','Cache-Control': 'no-cache','TE': 'Trailers'}

	data = '{"url":"'+url+'","domain":"tiny.one","alias":"","tags":[],"errors":{"errors":{}},"busy":true,"successful":false}'

	response = requests.post('https://tinyurl.com/app/api/create', headers=headers, cookies=cookies, data=data)

	secure = json.loads(response.content.decode())

	url3 = str(secure.get('data')[0].get('aliases')[0].get('tiny_url'))
	if url3:
		URL_LIST.append(url3)
	else:
		return 'INVALID'


	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0','Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Language': 'en-US,en;q=0.5','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','X-Requested-With': 'XMLHttpRequest','Origin': 'https://urlchill.com','DNT': '1','Connection': 'keep-alive','Referer': 'https://urlchill.com/','Pragma': 'no-cache','Cache-Control': 'no-cache'}

	data = {'url': url,'multiple': '0'}

	response = requests.post('https://urlchill.com/shorten', headers=headers, data=data)

	secure = json.loads(response.content.decode())

	if secure.get('short'):
		URL_LIST.append(secure.get('short'))
	else:
		return 'INVALID'

	return URL_LIST

def help():
	name  = "\033[0;1;3;38;5;46m"
	example = "\033[0;1;38;5;105m"
	to    = "\033[0;1;31m"
	module= "\033[0;1;38;5;117m"
	print(
		f"""
\033[0;38;5;123m
\033[0;38;5;123m██\033[0;91m╗  \033[0;38;5;123m██\033[0;91m╗\033[0;38;5;123m███████\033[0;91m╗\033[0;38;5;123m██\033[0;91m╗     \033[0;38;5;123m██████\033[0;91m╗ 
\033[0;38;5;123m██\033[0;91m║  \033[0;38;5;123m██\033[0;91m║\033[0;38;5;123m██\033[0;91m╔════╝\033[0;38;5;123m██\033[0;91m║     \033[0;38;5;123m██\033[0;91m╔══\033[0;38;5;123m██\033[0;91m╗
\033[0;38;5;123m███████\033[0;91m║\033[0;38;5;123m█████\033[0;91m╗  \033[0;38;5;123m██\033[0;91m║     \033[0;38;5;123m██████\033[0;91m╔╝
\033[0;38;5;123m██\033[0;91m╔══\033[0;38;5;123m██\033[0;91m║\033[0;38;5;123m██\033[0;91m╔══╝  \033[0;38;5;123m██\033[0;91m║     \033[0;38;5;123m██\033[0;91m╔═══╝ 
\033[0;38;5;123m██\033[0;91m║  \033[0;38;5;123m██\033[0;91m║\033[0;38;5;123m███████\033[0;91m╗\033[0;38;5;123m███████\033[0;91m╗\033[0;38;5;123m██\033[0;91m║     
\033[0;91m╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     
        

\033[0;1;4;38;5;41mHow To Use URLer?

\033[0;1;38;5;225mTo use URLer, you have to type the commands which follows down below.
URLer is a command line interface tool and works like console.
You have different commands and different methods to create URLs.

There are currently following modules available:

\033[0;1;4;38;5;41mModules{module}

>> {name}rstr <count>		{example}rstr 5		{module}Generate Random Strings
>> {name}swap <chars>		{example}swap secure	{module}Swap First And Last String
>> {name}rand <chars>		{example}rand secure	{module}Randomize A String
>> {name}strrev <chars>	{example}strrev secure	{module}String Reverse
>> {name}leet <chars>		{example}leet secure	{module}Leetmode For Strings
>> {name}gen_words <count>	{example}gen_words 10	{module}Generate Word(s)
>> {name}gen_url <count>	{example}gen_url 10	{module}Generate Url(s)
>> {name}check_sf <list>	{example}check_sf urls.txt	{module}Check Scampage Urls(Safebrowsing)
>> {name}short_url <url>	{example}short_url https://google.com	{module}Short URLs With GG.GG

\033[0;1;4;38;5;41mSpecial Combinations{module}

>> {name}murl <count>	{example}murl 10	{module}M-URL (Generated Word, Swap, Leetmode, Random Chars) \033[34;1m[\033[31;42;1m100%\033[0;34;1m]\033[0m{module}
>> {name}surl <count>	{example}surl 10	{module}S-URL (Generated Word, Randomize String, String Reverse, Leetmode) \033[34;1m[\033[31;42;1m100%\033[0;34;1m]\033[0m{module}
>> {name}lurl <count>	{example}lurl 10	{module}S-URL (Random String, String Reverse, Leetmode, Randomize String) \033[34;1m[\033[31;1;43m60%\033[0;34;1m]\033[0m{module}

\033[0;1;4;38;5;41mSpecial Characters & Commands{module}

>> {name}!<cmd>	{example}!ls	{module}Run Shell Commands
>> {name}clear	{example}clear	{module}Clear Screen
>> {name}c		{example}c	{module}Clear Screen
>> {name}?		{example}?	{module}Print This Help
>> {name}.		{example}.	{module}Exit
>> {name}e 		{example}e	{module}Exit
>> {name}!help	{example}!help	{module}Print This Help
>> {name}!exit	{example}!exit	{module}Exit
>> {name}.exit	{example}.exit	{module}Exit


		"""
		)

def main():
	if not dependencies_check():
		print(f"\033[34m[\033[31;1m!\033[0;34m] \033[37mError While Checking Dependencies: {error}")
		sys.exit(1)
	
	clear(platform)
	print(banner)
	print(f"\033[34;1m:: PLATFORM 	\033[31m{platform.upper()}\033[34m\033[37m")
	print(f"\033[34;1m:: USERNAME 	\033[31m{username.upper()}\033[34m\033[37m")
	print(f"\033[34;1m:: HOSTNAME 	\033[31m{hostname.upper()}\033[34m\033[37m")
	print(f"\033[34;1m:: RESULTS  	\033[31m{path.upper()}/{output_file.upper()}\033[34m\033[37m")
	print('')


	while True:
		cmd = input(f"\033[34m[\033[32m{username}\033[37m@\033[31m{hostname}\033[34m] \033[33m(\033[35;1m?\033[0;33m)\033[37m > ")
		if cmd == '?' or cmd == 'h' or cmd == 'help' or cmd == "!help":
			help()
		if re.findall("^![a-zA-Z0-9]{1,}$", cmd):
				os.system(cmd.split(sep='!')[1])
		if cmd == '!':	
			print(f"\033[34m[\033[31;1m!\033[0;34m] \033[37mPlease parse a command or read the manual. \033[34m(\033[32;1m!ls\033[34;1m)")
		if cmd == "." or cmd == "exit" or cmd == "e" or cmd == ".exit":
			sys.exit(print(byebye))
		if cmd == 'clear' or cmd == 'c':
			clear(platform)
		if re.findall("rstr [0-9]{1,"+str(max_count)+"}", cmd):
			print("\033[34m[\033[33;1m*\033[0;34m] \033[37mGenerated String : \033[33m"+ str(random_strings(' '.join(cmd.split(' ')[1:]))))
		if re.findall("swap [a-zA-Z]{1,}", cmd):
			print(f"\033[34m[\033[33;1m*\033[0;34m] \033[37mSwapped : \033[33m" + str(swap_chars(' '.join(cmd.split(' ')[1:]))))
		if re.findall("rand [a-zA-Z0-9]{1,}", cmd):
			print(f"\033[34m[\033[33;1m*\033[0;34m] \033[37mRandomized : \033[33m" + str(randomize(' '.join(cmd.split(' ')[1:]))))
		if re.findall("strrev [a-zA-Z0-9]{1,}", cmd):
			print(f"\033[34m[\033[33;1m*\033[0;34m] \033[37mReversed : \033[33m" + str(string_reverse(' '.join(cmd.split(' ')[1:]))))
		if re.findall("leet [a-zA-Z0-9]{1,}", cmd):
			print("\033[34m[\033[33;1m*\033[0;34m] \033[37mString L33t3d : \033[33m"+ str(leetmode(' '.join(cmd.split(' ')[1:]))))
		if re.findall("check_sf [a-zA-Z0-9]{1,}\.txt", cmd):
			print("\033[34m[\033[33;1m*\033[0;34m] \033[37mPreparing Checker...\033[0m")
			file = cmd.split(' ')[1]
			f = open(file, 'r').readlines()
			for url in f:
				url = url.replace("\n","")
				url_result = safebrowsing(url)
				if url_result == 'live':
					print(f"\033[34m[\033[33;1m*\033[0;34m] \033[37mURL \033[34m:: \033[37m{url} \033[34m(\033[32;1mLIVE\033[0;34m)\033[0m")
					saver(f"{path}/Scampage-Urls(live).txt",f"{url}\n")
				elif url_result == 'dead':
					print(f"\033[34m[\033[33;1m*\033[0;34m] \033[37mURL \033[34m:: \033[37m{url} \033[34m(\033[31;1mDEAD\033[0;34m)\033[0m")
					saver(f"{path}/Scampage-Urls(dead).txt",f"{url}\n")
				else:
					print(f"\033[34m[\033[33;1m*\033[0;34m] \033[37mURL \033[34m:: \033[37m{url} \033[34m(\033[34;1mERROR/UNKNOWN\033[0;34m)\033[0m")
					saver(f"{path}/Scampage-Urls(error-unknown).txt",f"{url}\n")

		if re.findall("gen_words [0-9]{1,}", cmd):
			if int(' '.join(cmd.split(' ')[1:])) == 1:
				print(f"\033[34m[\033[31;1m!\033[0;34m] \033[37mPlease generated minimal 2 words.")
			else:
				generate_words(' '.join(cmd.split(' ')[1:]))
		if re.findall("gen_url [0-9]{1,}", cmd):
			generate_url(' '.join(cmd.split(' ')[1:]))
		if re.findall("murl [0-9]{1,}", cmd):
			m_url(' '.join(cmd.split(' ')[1:]))
		if re.findall("surl [0-9]{1,}", cmd):
			s_url(' '.join(cmd.split(' ')[1:]))
		if re.findall("lurl [0-9]{1,}", cmd):
			l_url(' '.join(cmd.split(' ')[1:]))
		if re.findall("short_url (http|https)?(:\/\/)?(.*?)\/?", cmd):
			url = short_url(' '.join(cmd.split(' ')[1:]))
			if url != 'Invalid':
				for u in url:
					print(f"\033[34m[\033[32;1m*\033[0;34m] \033[37mShorten URL: \033[32m{u}")
					saver(f"{path}/{output_file}", f"{u.lower()}\n")
if __name__ == '__main__':
	main()
