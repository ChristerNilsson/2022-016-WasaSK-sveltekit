import json
import time
import datetime
from os import scandir
from urllib.parse import unquote
from os.path import getctime
import dateutil.parser as parser
import re
from urllib import request

UPDATE = True

FORBIDDEN = "-0123456789"
datum = re.compile(r'(\d\d\d\d-\d\d-\d\d)$')

allWords = set()

stats = {
	'updated': str(datetime.datetime.now())[0:16],
	'items':0,
	'files':0,
	'legacy':0,
	'legacyBytes':0,
	'words':0,
	'posts':0
}

def pr(s): return s.replace("_"," ")
def split(s): return list(filter(lambda x: x != "",s.split(' ')))
def tel(s): return s[0:3] + ' - ' + s[4:7] + " " + s[7:9] + " " + s[9:11]

def level(s): return s.count('\t')

def check(filename):
	if filename.startswith('/'): return True
	if filename.startswith('http'): return True
	if filename.endswith('.md'): return filename in files_md
	return '/' + filename in files_files

def indented2object(raw):
	def pop(n):
		for i in range(n): stack.pop()
	lst = raw.split('\n')
	stats['items'] = len(lst)
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
	def recurse(path):
		for name in [f for f in scandir(path)]:
			if name.is_dir():
				recurse(name)
			else:
				res.append(name.path[7:].replace("\\",'/'))
	res = []
	recurse(path)
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

def extractWords(s):
	global allWords
	s = unquote(s)
	for ch in "`'&<>()[]{}+*/|:;!?,._#$@%=\t\n\r" + '"' :
		s = s.replace(ch,' ')
	s = s.replace ("\\n"," ")
	s = s.replace ("\\t"," ")
	words = [word.lower() for word in s.split(' ')]
	temp = []
	for word in words:
		temp += extraWord(word)
	words = temp

	words = set(words)
	words = [word for word in words if " " + word + " " not in STOPWORDS]
	words = [word for word in words if accepted(word)]
	allWords = allWords.union(words)
	words.sort()
	stats['words'] += len(words)
	return ' '.join(words)


def processFiles(dir,filenames,prefix=""):
	for filename in filenames:
		if filename.endswith('.JPG'): continue
		path = dir + filename
		with open(path, 'r', encoding='utf-8') as f:
			s = f.read()
			ti_c = getctime(path)
			c_ti = time.ctime(ti_c)
			stamp = parser.parse(c_ti)
			stamp = stamp.isoformat().replace('T',' ')
			words = extractWords(filename + ' ' + s)
			mdData.append([stamp, prefix + filename, words])

def processLegacyFiles():
	with open('legacy.txt', 'r', encoding="utf-8") as f:
		s = f.read()
		arr = s.split("\n")
		for filename in arr:
			if len(filename) == 0: continue
			if "#" in filename: continue
			[stamp,filename] = filename.split(' ')
			path = 'legacy/' + filename
			with open(path, 'r', encoding='utf-8') as g:
				s = g.read()
				words = extractWords(filename + ' ' + stamp + ' ' + s)
				mdData.append([stamp, path, words])
				stats['legacy'] += 1
				stats['legacyBytes'] += len(s)


def readLegacyFiles():
	with open('legacy.txt', 'r', encoding="utf-8") as f:
		s = f.read()
		arr = s.split("\n")
		for filename in arr:
			if len(filename) == 0: continue
			if "#" in filename: continue
			[stamp,filename] = filename.split(' ')

			with request.urlopen('http://wasask.se/' + filename) as f:
				s = f.read()

			print(filename)

			if filename in "Veckobrev_v4.php Veckobrev_v5.php Veckobrev_v36.php Veckobrev_v40.php Veckobrev_v48.php".split(' '):
				t = s.decode("Windows-1252")
			else:
				t = s.decode("utf-8","backslashreplace")

			with open('legacy/' + filename, 'w', encoding='utf-8') as g:
				g.write(t)

with open('stoppord.txt', 'r', encoding="utf-8") as f:
	STOPWORDS = ' '+ f.read().replace("\n"," ")

start = time.time()

mdData = []

##### readLegacyFiles() # OBS! Kör över manuella ändringar!

files_md = getNames("src/md")
files_files = getNames("src/lib/files")

processFiles('src/md/',files_md)
processLegacyFiles()

menu = readMenuTree()

stats['files'] = len(files_files)
stats['posts'] = len(files_md)
stats['words'] = len(allWords)

mdData.sort()
mdData.reverse()

hash = {}
for [datum,key,words] in mdData:
	hash[key] = [datum,words]

total = {'menu':menu, 'md':hash, 'stats':stats}

with open("src/lib/site.json", "w", encoding="utf8") as f:
	if UPDATE: dumpjson(total,f)

print('Körtid:',round(time.time()-start,3),'s')
print(stats)
