from BeautifulSoup import BeautifulSoup
from datetime import datetime
import urllib2
import re

# 
# A script getting deck by formatting "cockatrice" from hearthpwn in batch
#   Note:
#     Working in Python 2.7.10
#                                       by orczhou@gmail.com@2016-03-19
#

for page in range(1,2):
  now_time = datetime.now()
  print  "[%s]Start to get page 1 of top month deck......" % now_time.strftime('%Y-%m-%d %H:%M:%S')
  # filter-deck-tag=4 : Top Month Deck
  url_topmonth = "http://www.hearthpwn.com/decks?filter-deck-tag=4&page=" + str(page)
  page = urllib2.urlopen(url_topmonth)
  soup = BeautifulSoup(page.read())
  
  decks = soup.findAll(attrs={"class" : "tip"})
  for deck in decks:
    #<span class="tip" title='&lt;div class="deck-tooltip"&gt;&lt;h4&gt;Warlock Deck&lt;/h4&gt;&lt;span class="tooltip-cards-count t-deck-card-count-minions"&gt;21 Minions&lt;/span&gt;&lt;span class="tooltip-cards-count t-deck-card-count-spells"&gt;9 Spells&lt;/span&gt;&lt;span class="tooltip-cards-count t-deck-card-count-weapons"&gt;0 Weapons&lt;/span&gt;&lt;/div&gt;'>
    #<a href="/decks/421001-kolentos-quicker-combo-renolock">Kolento&#x27;s quicker combo renolock</a>
    #</span>
    p = re.compile('<span.*><a href="/decks/(\d+)\-(.*)">(.*)</a></span>');
    m = p.match(str(deck))
    deck_id = m.group(1)
    deck_name = m.group(2)
    cockatrice = "http://www.hearthpwn.com/decks/" + deck_id + "/export/1"
  
    print "  Get deck from deck page:" + cockatrice 
    u = urllib2.urlopen(cockatrice)
    html = u.read()
    f = open("./tmp/"+deck_name+".txt", 'wb')
    f.write(html.replace('&#x27;',"'"))
    print "  Saved in the file " + deck_name + ".txt\n"
    f.close()
