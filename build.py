import json
import time
import datetime
from os import scandir
from urllib.parse import unquote
from os.path import getctime
import dateutil.parser as parser
import re

UPDATE = True

FORBIDDEN = "-0123456789"
datum = re.compile(r'(\d\d\d\d-\d\d-\d\d)$')

stats = {
	'updated': str(datetime.datetime.now())[0:16],
	'items':0,
	'files':0,
	'words':0,
	'posts':0
}

def pr(s): return s.replace("_"," ")
def split(s): return list(filter(lambda x: x != "",s.split(' ')))
def tel(s): return s[0:3] + ' - ' + s[4:7] + " " + s[7:9] + " " + s[9:11]

def level(s): return s.count('\t')

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
			if filename.startswith('/') or filename.startswith('http') or filename.endswith('.md') or filename.endswith('.html') and filename in files_md or filename in files_files:
				pos[key] = filename
			else:
				print('Filen saknas:', filename)

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
	for ch in FORBIDDEN:
		if ch in word: return False
	return True

def extractWords(s):
	s = unquote(s)
	for ch in "`'&<>()[]{}+*/|:;!?,._#$@%=\t\n" + '"':
		s = s.replace(ch,' ')
	words = [word.lower() for word in s.split(' ')]
	words = set(words)
	words = [word for word in words if " " + word + " " not in STOPWORDS]
	words = [word for word in words if accepted(word)]
	words.sort()
	stats['words'] += len(words)
	return ' '.join(words)

start = time.time()

files_md = getNames("src/md")
#files_html = getNames("src/html")
files_files = getNames("src/lib/files")

def processFiles(dir,filenames):
	for filename in filenames:
		if filename.endswith('.JPG'): continue
		path = dir + filename
		with open(path, 'r', encoding="utf-8") as f:
			ti_c = getctime(path)
			c_ti = time.ctime(ti_c)
			stamp = parser.parse(c_ti)
			stamp = stamp.isoformat().replace('T',' ')
			s = f.read()
			words = extractWords(filename + ' ' + s)
			mdData[filename] = [stamp, words]


with open('stoppord.txt', 'r', encoding="utf-8") as f:
	STOPWORDS = ' '+ f.read().replace("\n"," ")

mdData = {}
processFiles('src/md/',files_md)
# processFiles('src/html/',files_html)

menu = readMenuTree()
stats['files'] = len(files_files)
stats['posts'] = len(files_md)
total = {'menu':menu, 'md':mdData, 'stats':stats}

with open("src/lib/site.json", "w", encoding="utf8") as f:
	if UPDATE: dumpjson(total,f)

print('Körtid:',round(time.time()-start,3),'s')
