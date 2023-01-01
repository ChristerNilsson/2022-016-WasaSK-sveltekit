import json
import time
import datetime
from os import scandir
from urllib.parse import unquote
import re
from urllib import request
import html2text
import requests

UPDATE = True

datum = re.compile(r'(\d\d\d\d-\d\d-\d\d)$')

allWords = set()

# freq = {}
letters = {}

stats = {
	'updated': str(datetime.datetime.now())[0:16],
	'menuItems':0,
	'mdPosts':0,
	'mdBytes': 0,
	'phpPosts':0,
	'phpBytes':0,
	'blogPosts':0,
	'blogBytes':0,
	'uniqWords':0,
	'wordBytes':0,
	'files': 0,

	'ålder': {'Junior':0,'Senior':0,'_':0,},
	'typ'  : {'Träning':0,'Resultat':0,'Program':0,'Inbjudan':0,'Notis':0,'Game':0,'Diverse':0,'_':0},
	'lag'  : {'Individ':0,'Lag':0,'_':0},
	'nivå' : {'KM':0,'DM':0,'SM':0,'NM':0,'EM':0,'WM':0,'_':0},
	'tid'  : {'Blixt':0,'Snabb':0,'Lång':0,'_':0},
	'kön'  : {'Man':0,'Kvinna':0,'_':0},
	'år'   : {},
	'månad': {"Jan":0,"Feb":0,"Mar":0,"Apr":0,"Maj":0,"Jun":0,"Jul":0,"Aug":0,"Sep":0,"Okt":0,"Nov":0,"Dec":0},

}

def pr(s): return s.replace("_"," ")
def split(s): return list(filter(lambda x: x != "",s.split(' ')))
def tel(s): return s[0:3] + ' - ' + s[4:7] + " " + s[7:9] + " " + s[9:11]

def level(s): return s.count('\t')

def check(filename):
	if filename.startswith('/'): return True
	if filename.startswith('http'): return True
	if filename.startswith('common'):return 'src/' + filename in files_common
	if filename.startswith('files'):
		return 'src/lib/' + filename in files_files
	if filename.endswith('.md'): return filename in files_md
	return '/' + filename in files_files

def indented2object(raw):
	def pop(n):
		for i in range(n): stack.pop()
	lst = raw.split('\n')
	stats['menuItems'] = len(lst)
	levels = [level(item) for item in lst]
	tree = {}
	stack = []
	for i in range(len(lst)):
		if lst[i] == "": continue
		if i != 0:
			delta = levels[i] - levels[i-1]
			if delta < 0: pop(len(stack) - levels[i])
			elif delta == 0: stack.pop()
		stack.append(lst[i].strip())
		pos = tree
		for j in range(len(stack)-1):
			pos = pos[stack[j]]

		name = stack[-1]
		arr = name.split(': ')
		if len(arr)==1:
			pos[name] = {}
		else:
			key,filename = arr
			if check(filename):
				pos[key] = filename
			else:
				print('Filen', filename, 'i menu.tree saknas i katalogen')

	return tree

def getNames(path):
	res = []
	for name in [f for f in scandir(path)]:
		res.append(name.path.replace("\\", '/'))
	res.sort()
	res.reverse()
	return res

def readMenuTree():
	with open('menu.tree', 'r', encoding="utf-8") as f:
		return indented2object(f.read())

def dumpjson(data,f):
	s = json.dumps(data, ensure_ascii=False, separators=(",", ":"), sort_keys=False)
	s = s.replace("],","],\n")
	s = s.replace(":{",":\n{")
	# s = s.replace('},"','},\n"')
	# s = s.replace('","','",\n"')
	if UPDATE: f.write(s)

def accepted(word):
	if datum.match(word): return True
	for ch in "0123456789":
		if ch in word: return False
	return True

def extraWord(word):
	if datum.match(word):
		return [word]
	else:
		return word.split('-')

# Behåller ordningen, men tar bort senare förekomster.
# Tillåter inte siffror, förutom i datum
def extractWords(s):
	global allWords

	s = unquote(s).lower()

	for ch in "`'&<>()[]{}+*/|:;!?,._#$@%=\t\n\r" + '"”½’…´·‘“—šó¨' :
		s = s.replace(ch,' ')
	s = s.replace ("\\n"," ")
	s = s.replace ("\\t"," ")

	res = s.lower().split(' ')
	words = " ".join(res).split(' ')

	temp = []
	for word in words:
		temp += extraWord(word)
	words = temp

	# words = [word for word in words if word!='' and " " + word + " " not in STOPWORDS]
	words = [word for word in words if accepted(word)]

	allWords = allWords.union(words)
	stats['uniqWords'] += len(words)

	# Skippa ord andra gången de förekommer
	hash = {}
	next = []
	for word in words:
		if word not in hash:
			next.append(word)
			hash[word] = 1
	words = next

	# for word in words:
	# 	if word not in freq: freq[word] = 0
	# 	freq[word] += 1

	words.sort()
	words = " ".join(words)

	# words = words.replace('type text css ','').replace('link rel stylesheet ','').replace('strong ','')
	stats['wordBytes'] += len(words)
	for ch in words:
		letters[ch] = 1
	return words

# def processCommon(dir,filenames):
# 	for filename in filenames:
# 		path = dir + filename
# 		with open(path, 'r', encoding='utf-8') as f:
# 			s = f.read()
# 			ti_c = getctime(path)
# 			c_ti = time.ctime(ti_c)
# 			stamp = parser.parse(c_ti)
# 			stamp = stamp.isoformat().replace('T',' ')
# 			words = extractWords(filename + ' ' + s)
# 			posts.append([stamp, filename, words])
# 			stats['mdPosts'] += 1
# 			stats['mdBytes'] += len(s)

def handle(attr,value):
	if value not in stats[attr]: stats[attr][value] = 0
	stats[attr][value] += 1

MONTH = {'01':'Jan','02':'Feb','03':'Mar','04':'Apr','05':'Maj','06':'Jun','07':'Jul','08':'Aug','09':'Sep','10':'Okt','11':'Nov','12':'Dec'}
AGE   = {'J':'Junior','S':'Senior','_':'_'}
TYP   = {'T':'Träning','D':'Diverse','R':'Resultat','P':'Program','I':'Inbjudan','N':'Notis','G':'Game','_':'_'}
TEAM  = {'L':'Lag','I':'Individ','_':'_'}
LEVEL = {'K':'KM','D':'DM','S':'SM','N':'NM','E':'EM','W':'WM','_':'_'}
TIME  =  {'B':'Blixt','S':'Snabb','L':'Lång','_':'_'}
SEX   =  {'K':'Kvinna','M':'Man','_':'_'}

def makeStats(year,month,age,typ,team,level,time,sex):
	handle('år',year)
	handle('månad',MONTH[month])
	handle('ålder',AGE[age])
	handle('typ',TYP[typ])
	handle('lag',TEAM[team])
	handle('nivå',LEVEL[level])
	handle('tid',TIME[time])
	handle('kön',SEX[sex])

def getAttr(keys,s):
	keys = keys.split(' ')
	arr = s.split('\n')
	res = {}
	for row in arr:
		for key in keys:
			if row.startswith(key):
				pair = row.split(':')
				res[pair[0].strip()] = pair[1].strip()
				if len(res) == len(keys): return res
	return {}

def processMD(filenames):
	for filename in filenames:
		path = filename
		with open(path, 'r', encoding='utf-8') as f:
			s = f.read()
		hash = getAttr('date attr',s)
		if len(hash) != 2:
			print('missing date or attr in meta data for',filename)
			continue
		date = hash['date']
		attr = hash['attr']
		year = date[0:4]
		month = date[5:7]
		age = attr[0]
		typ = attr[1]
		team = attr[2]
		level = attr[3]
		time = attr[4]
		sex = attr[5]
		makeStats(year,month,age,typ,team,level,time,sex)
		words = extractWords(filename + ' ' + s)
		posts.append([{'date':date,'attr':attr,'size':len(s)}, filename.replace('src/',''), words])
		stats['mdPosts'] += 1
		stats['mdBytes'] += len(s)

def fetch(key): return list(map(lambda word: word[0], dimensions[key].split(' ')))

def processPHP():

	h = html2text.HTML2Text()
	h.ignore_links = True
	h.ignore_images = True

	letters = {}
	letters["ålder"] = fetch('ålder')
	letters["typ"]   = fetch('typ')
	letters["lag"]   = fetch('lag')
	letters["nivå"]  = fetch('nivå')
	letters["tid"]   = fetch('tid')
	letters["kön"]   = fetch('kön')

	attrComb = {}
	with open('php.txt', 'r', encoding="utf-8") as f:
		for row in f.read().split("\n"):
			if len(row) == 0: continue
			if "#" in row: continue
			row = row.split(' ')
			date = row[0]
			attr = row[1]
			filename = row[2]

			[age,typ,team,level,time,sex] = attr
			year = date[0:4]
			month = date[5:7]
			# print(filename)
			makeStats(year,month,age,typ,team,level,time,sex)

			key = row[1]
			if key not in attrComb: attrComb[key] = []
			attrComb[key].append(filename)

			if len(date) != 10: print('date has wrong length',filename)
			if date[0:4] not in dimensions['år']: print('missing year',date[0:4],filename)
			if age != '_'   and age   not in letters['ålder']: print('missing age',age,filename)
			if typ != '_'   and typ   not in letters['typ']:   print('missing typ',typ,filename)
			if team != '_'  and team  not in letters['lag']:   print('missing team',team,filename)
			if level != '_' and level not in letters['nivå']:  print('missing level',level,filename)
			if time != '_'  and time  not in letters['tid']:   print('missing time',time,filename)
			if sex != '_'   and sex   not in letters['kön']:   print('missing sex',sex,filename)

			path = 'php/' + filename
			if filename == 'test.php':
				z=99
			with open(path, 'r', encoding='utf-8') as g:
				s = g.read()

				text = h.handle(s)

				words = extractWords(filename + ' ' + date+ ' ' + text)
				posts.append([{'date':date,'attr':attr,'size':len(s)}, path, words])
				stats['phpPosts'] += 1
				stats['phpBytes'] += len(s)

urls = []
def extractURL(buffer):
	prefix = "https://www.wasask.se/aaawasa/wordpress/wp-content"
	starter = '<h2 class="entry-title" itemprop="headline"><a href="'
	ender = '" rel="bookmark">'
	url = ""
	for line in buffer:
		if starter in line:
			p = line.index(starter)+len(starter)
			q = line.index(ender)
			url = line[p:q-1]
			# if "https://www.wasask.se/aaawasa/wordpress/wp-content" in url:
			# 	urls.append(url)
		if 'datetime' in line and url != "":
			p = line.index('datetime')
			date = line[p+10:p+29].replace('T',' ')
			if prefix in url:
				urls.append(date + " ______ " + url)
			url = ''

def getWasaBlog_1():
	### Reads 24 pages in Wasa blog and writes 24 files
	url = "https://www.wasask.se/aaawasa/wordpress/page/"
	for i in range(1,24):
		print(i)
		req = requests.get(url=url+str(i))
		with open('wasa/' + str(i) + ".txt", 'w', encoding='utf-8') as g:
			g.write(req.text)

def getWasaBlog_2():
	### Reads 24 files and extract all relevant URL:S to ONE file, wasa.txt witd date, time, attr and full url
	url = "https://www.wasask.se/aaawasa/wordpress/page/"
	for i in range(1,24):
		with open('wasa/' + str(i) + ".txt", 'r', encoding='utf-8') as g:
			s = g.read()
			arr = s.split('\n')
			buffer = []
			state = 0
			for line in arr:
				if '<article' in line:
					state = 1
				if state == 1:
					buffer.append(line)
				if '</article' in line:
					state = 2
				if state == 2:
					#print(buffer)
					extractURL(buffer)
					state = 0
					buffer = []
	urls.sort()
	urls.reverse()
	with open('wasa.txt', 'w', encoding='utf-8') as h:
		h.write("\n".join(urls))

	print(len(urls))

def getWasaBlog_3():
	### reads 223 urls, fetches their content and saves full html content in wasa/files
	with open('wasa.txt', 'r', encoding='utf-8') as g:
		s = g.read()
		files = s.split('\n')
		for file in files:
			[date,time,attr,url] = file.split(' ')
			req = requests.get(url=url)
			p = file.rindex('/')
			filename = "wasa/files/" + file[p+1:] + '.html'
			print(filename)
			with open(filename, 'w', encoding='utf-8') as f:
				f.write(req.text)

def getWasaBlog_4():
	### read 223 html files, extract text and words, store in json file together with markdown files
	prefix = 'https://www.wasask.se/aaawasa/wordpress/wp-content/'

	h = html2text.HTML2Text()
	h.ignore_links = True
	h.ignore_images = True

	with open('wasa.txt', 'r', encoding='utf-8') as g:
		s = g.read()
		files = s.split('\n')
		for file in files:
			[date,time,attr,url] = file.split(' ')
			year = date[0:4]
			month = date[5:7]
			[age, typ, team, level, time, sex] = attr
			makeStats(year, month, age, typ, team, level, time, sex)

			p = file.rindex('/')
			filename = "wasa/files/" + file[p+1:] + '.html'
			with open(filename, 'r', encoding='utf-8') as f:
				html = f.read()
			size = len(html)
			text = h.handle(html)
			words = extractWords(date + ' ' + text)
			filename = filename.replace('/files/','/words/').replace('.html','.txt')
			print(filename)

			# with open(filename, 'w', encoding='utf-8') as f:
			# 	f.write(words)
			posts.append([{'date': date, 'attr': attr, 'size': size}, url.replace(prefix,'blog/'), words])
			stats['blogPosts'] += 1
			stats['blogBytes'] += size

def readPhpFiles():
	with open('php.txt', 'r', encoding="utf-8") as f:
		s = f.read()
		arr = s.split("\n")
		for row in arr:
			if len(row) == 0: continue
			if "#" in row: continue

			[stamp,age,typ,team,level,sex,filename] = row.split(' ')

			with request.urlopen('http://wasask.se/' + filename) as f:
				s = f.read()

			print(filename)

			if filename in "Veckobrev_v4.php Veckobrev_v5.php Veckobrev_v36.php Veckobrev_v40.php Veckobrev_v48.php".split(' '):
				t = s.decode("Windows-1252")
			else:
				t = s.decode("utf-8","backslashreplace")

			with open('php/' + filename, 'w', encoding='utf-8') as g:
				g.write(t)


def readDimensions():
	with open('src/lib/data/dimensions.json', 'r', encoding="utf-8") as f:
		return json.load(f)

start = time.time()
posts = []

# getWasaBlog_1()
# getWasaBlog_2()
# getWasaBlog_3()
getWasaBlog_4()

# def invertDimensions(dimensions):
# 	res = {}
# 	for key in dimensions:
# 		for key2 in dimensions[key].split(' '):
# 			res[key2] = key
# 	return res

dimensions = readDimensions()
# invDim = invertDimensions(dimensions)

#with open('stoppord.txt', 'r', encoding="utf-8") as f:
#	STOPWORDS = ' '+ f.read().replace("\n"," ")
STOPWORDS = ""

#readPhpFiles() # OBS! Kör över manuella ändringar!

files_common = getNames("src/common")
files_md = getNames("src/md")
files_files = getNames("src/lib/files")

# processCommon(files_common)
processMD(files_md)
processPHP()

menu = readMenuTree()

stats['files'] = len(files_files)
#stats['mdPosts'] = len(files_md)
stats['uniqWords'] = len(allWords)

posts = sorted(posts, key=lambda item: item[0]['date'])
posts.reverse()

hash = {}
for [datum,key,words] in posts:
	hash[key] = [datum,words]

total = {'posts':hash, 'stats':stats, 'menu':menu}

with open("src/lib/data/site.json", "w", encoding="utf8") as f:
	if UPDATE: dumpjson(total,f)

print('Körtid:',round(time.time()-start,3),'s')
print(stats)
# print(letters)

# arr = []
# for word in freq:
# 	arr.append([freq[word],word])
# arr.sort()
# print(arr)
