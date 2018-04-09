from lxml import html
import requests
import pprint

page = requests.get('http://www.fussball.de/spieltag/u-17-b-jun-bayernliga-bayern-b-junioren-bayernliga-b-junioren-saison1718-bayern/-/staffel/020C68FGC4000000VS54898DVSDVETU6-G#!/section/matches')
tree = html.fromstring(page.content)

clubname = tree.xpath('//div[@class="club-name"]/text()')

#for c in clubname:
   # print(c)

pprint.pprint(clubname)