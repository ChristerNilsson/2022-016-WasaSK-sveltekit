import json
import time
import datetime
from os import scandir
from urllib.parse import unquote
# from os.path import getctime
# import dateutil.parser as parser
import re
from urllib import request

UPDATE = True

FORBIDDEN = "-0123456789"
datum = re.compile(r'(\d\d\d\d-\d\d-\d\d)$')

allWords = set()

freq = {}
letters = {}

stats = {
	'updated': str(datetime.datetime.now())[0:16],
	'menuItems':0,
	'mdPosts':0,
	'mdBytes': 0,
	'phpPosts':0,
	'phpBytes':0,
	'uniqWords':0,
	'wordBytes':0,
	'files': 0,
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
	s = s.replace('},"','},\n"')
	s = s.replace('","','",\n"')
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

	words = [word for word in words if word!='' and " " + word + " " not in STOPWORDS]
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

	for word in words:
		if word not in freq: freq[word] = 0
		freq[word] += 1

	words = ' '.join(words)

	words = words.replace('type text css ','').replace('link rel stylesheet ','').replace('strong ','')
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

def processMD(dir, filenames):
	for filename in filenames:
		path = filename
		with open(path, 'r', encoding='utf-8') as f:
			attributes = filename[7:24]
			s = f.read()
			words = extractWords(filename + ' ' + s)
			posts.append([attributes, filename.replace('src/',''), words])
			stats['mdPosts'] += 1
			stats['mdBytes'] += len(s)

def processPHP():

	def fetch(key): return list(map(lambda word: word[0], dimensions[key].split(' ')))

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
			filename = row[2]

			[age,typ,team,level,time,sex] = row[1]

			key = row[1]
			if key not in attrComb: attrComb[key] = []
			attrComb[key].append(filename)

			if len(date) != 10: print('date har wrong length',filename)
			if date[0:4] not in dimensions['år']: print('missing year',date[0:4],filename)
			if age != '_'   and age   not in letters['ålder']: print('missing age',age,filename)
			if typ != '_'   and typ   not in letters['typ']:   print('missing typ',typ,filename)
			if team != '_'  and team  not in letters['lag']:   print('missing team',team,filename)
			if level != '_' and level not in letters['nivå']:  print('missing level',level,filename)
			if time != '_'  and time  not in letters['tid']:   print('missing time',time,filename)
			if sex != '_'   and sex   not in letters['kön']:   print('missing sex',sex,filename)

			path = 'php/' + filename
			with open(path, 'r', encoding='utf-8') as g:
				s = g.read()
				words = extractWords(filename + ' ' + date+ ' ' + s)
				posts.append([row[0]+' '+row[1], path, words])
				stats['phpPosts'] += 1
				stats['phpBytes'] += len(s)

		#print('Sällsynta attribut-kombinationer:')
		#for key in attrComb:
			#if len(attrComb[key]) <= 10:
				#print(key,attrComb[key])
		#print('')

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
	with open('src/lib/dimensions.json', 'r', encoding="utf-8") as f:
		return json.load(f)

dimensions = readDimensions()

with open('stoppord.txt', 'r', encoding="utf-8") as f:
	STOPWORDS = ' '+ f.read().replace("\n"," ")

start = time.time()

posts = []

#readPhpFiles() # OBS! Kör över manuella ändringar!

files_common = getNames("src/common")
files_md = getNames("src/md")
files_files = getNames("src/lib/files")

# processCommon(files_common)
processMD('md/',files_md)
processPHP()

menu = readMenuTree()

stats['files'] = len(files_files)
#stats['mdPosts'] = len(files_md)
stats['uniqWords'] = len(allWords)

posts.sort()
posts.reverse()

hash = {}
for [datum,key,words] in posts:
	hash[key] = [datum,words]

total = {'menu':menu, 'posts':hash, 'stats':stats}

with open("src/lib/site.json", "w", encoding="utf8") as f:
	if UPDATE: dumpjson(total,f)

print('Körtid:',round(time.time()-start,3),'s')
print(stats)
# print(letters)

# arr = []
# for word in freq:
# 	arr.append([freq[word],word])
# arr.sort()
# print(arr)
