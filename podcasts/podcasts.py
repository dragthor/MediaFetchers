import feedparser
import sys

list = { 
	'hanselminutes':'http://feeds.podtrac.com/9dPm65vdpLL1', 
	'dotnetrocks':'http://www.pwop.com/feed.aspx?show=dotnetrocks&filetype=master',
	'runasradio':'http://feeds.feedburner.com/RunasRadio',
	'helloworld':'http://hwpod.libsyn.com/rss',
	'focusonthefamily':'http://feeds.feedburner.com/FocusOnTheFamilyDailyBroadcast?format=xml'
}

top = 10
key = 'hanselminutes'
url = ''

if len(sys.argv) > 1:
	key = sys.argv[1]

if len(sys.argv) > 2:
	try:
		top = int(sys.argv[2])
	except ValueError:
		top = 10

try:
	url = list[key]
except KeyError:
	print('Invalid postcast key name.')
	sys.exit()
		
d = feedparser.parse(url)

title = d.feed.title
lastUpdate = d.feed.updated
#d.feed.updated_parsed

print('---------------------------------------------------------')
print(title + ' - updated on ' + lastUpdate)
print('---------------------------------------------------------')
print('\n')

for entry in d.entries[:top]:
	print(entry.title)
	print(entry.published)
	links = entry.links
	for link in links:
		print(link.href)
	print('\n')
