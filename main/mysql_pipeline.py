from datetime import datetime
import hashlib
import sys

import MySQLdb
from TwitterAPI import TwitterAPI
from colorama import Fore, Style
from pytz import timezone
from scrapy.exceptions import DropItem
from scrapy.http import Request

from items import *


# Convert time to EST.
DATE_CONVERT = datetime.now(timezone('US/Eastern'))
DATE = DATE_CONVERT.strftime("%m-%d-%Y|%H:%M:%S")

# MYSQL pipleline for storing.
class MYSQL_Pipeline(object):
    
  def __init__(self):
    # Database connection info. (host, user, password, database)
    self.conn = MySQLdb.connect(host=' HOST NAME HERE ', user=' USER NAME HERE ', passwd=' PASSWORD HERE ', db=' DATABASE NAME HERE ', charset="utf8", use_unicode=True)
    self.conn.ping(True)
    self.cursor = self.conn.cursor()
    
  # Process the item and insert into database.
  def process_item(self, item, spider):
    try:
        # Insert item into kith table.
        if isinstance(item, KithItem):
            self.cursor.execute("INSERT INTO kith (name, link, image, date) VALUES (%s, %s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), item['image'].encode('utf-8'), DATE))
            
        # Insert item into ruvilla table.
        elif isinstance(item, RuvillaItem):
            self.cursor.execute("INSERT INTO ruvilla (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into footlocker table.
        elif isinstance(item, FootLockerItem):
            self.cursor.execute("INSERT INTO footlocker (name, link, image, date) VALUES (%s, %s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), item['image'].encode('utf-8'), DATE))
            
        # Insert item into footaction table.
        elif isinstance(item, FootActionItem):
            self.cursor.execute("INSERT INTO footaction (name, link, image, date) VALUES (%s, %s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), item['image'].encode('utf-8'), DATE))
            
        # Insert item into champs table.
        elif isinstance(item, ChampsItem):
            self.cursor.execute("INSERT INTO champs (name, link, image, date) VALUES (%s, %s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), item['image'].encode('utf-8'), DATE))
            
        # Insert item into eastbay table.
        elif isinstance(item, EastBayItem):
            self.cursor.execute("INSERT INTO eastbay (name, link, image, date) VALUES (%s, %s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), item['image'].encode('utf-8'), DATE))
            
        # Insert item into finishline table.
        elif isinstance(item, FinishLineItem):
            self.cursor.execute("INSERT INTO finishline (name, link, image, date) VALUES (%s, %s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), item['image'].encode('utf-8'), DATE))
            
        # Insert item into adidas table.
        elif isinstance(item, AdidasItem):
            self.cursor.execute("INSERT INTO adidas (name, link, image, date) VALUES (%s, %s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), item['image'].encode('utf-8'), DATE))
            
        # Insert item into nike table.
        elif isinstance(item, NikeItem):
            self.cursor.execute("INSERT INTO nike (name, link, image, date) VALUES (%s, %s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), item['image'].encode('utf-8'), DATE))
            
        # Insert item into footshop table.
        elif isinstance(item, FootShopItem):
            self.cursor.execute("INSERT INTO footshop (name, link, image, date) VALUES (%s, %s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), item['image'].encode('utf-8'), DATE))
            
        # Insert item into caliroots table.
        elif isinstance(item, CalirootsItem):
            self.cursor.execute("INSERT INTO caliroots (name, link, image, date) VALUES (%s, %s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), item['image'].encode('utf-8'), DATE))
            
        # Insert item into afew table.
        elif isinstance(item, AfewItem):
            self.cursor.execute("INSERT INTO afew (name, link, image, date) VALUES (%s, %s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), item['image'].encode('utf-8'), DATE))
            
        # Insert item into einhalb table.
        elif isinstance(item, EinhalbItem):
            self.cursor.execute("INSERT INTO einhalb (name, link, image, date) VALUES (%s, %s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), item['image'].encode('utf-8'), DATE))
            
        # Insert item into end table.
        elif isinstance(item, EndItem):
            self.cursor.execute("INSERT INTO end (name, link, image, date) VALUES (%s, %s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), item['image'].encode('utf-8'), DATE))
            
        # Insert item into sns table.
        elif isinstance(item, SNSItem):
            self.cursor.execute("INSERT INTO sns (name, link, image, date) VALUES (%s, %s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), item['image'].encode('utf-8'), DATE))
            
        # Insert item into goodwillout table.
        elif isinstance(item, GoodWillOutItem):
            self.cursor.execute("INSERT INTO goodwillout (name, link, image, date) VALUES (%s, %s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), item['image'].encode('utf-8'), DATE))
            
        # Insert item into tint table.
        elif isinstance(item, TintItem):
            self.cursor.execute("INSERT INTO tint (name, link, image, date) VALUES (%s, %s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), item['image'].encode('utf-8'), DATE))
            
        # Insert item into overkill table.
        elif isinstance(item, OverkillItem):
            self.cursor.execute("INSERT INTO overkill (name, link, image, date) VALUES (%s, %s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), item['image'].encode('utf-8'), DATE))
            
        # Insert item into footdistrict table.
        elif isinstance(item, FootDistrictItem):
            self.cursor.execute("INSERT INTO footdistrict (name, link, image, date) VALUES (%s, %s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), item['image'].encode('utf-8'), DATE))
            
        # Insert item into size table.
        elif isinstance(item, SizeItem):
            self.cursor.execute("INSERT INTO size (name, link, image, date) VALUES (%s, %s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), item['image'].encode('utf-8'), DATE))
            
        # Insert item into ycmc table.
        elif isinstance(item, YCMCItem):
            self.cursor.execute("INSERT INTO ycmc (name, link, image, date) VALUES (%s, %s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), item['image'].encode('utf-8'), DATE))
            
        # Insert item into city table.
        elif isinstance(item, CityItem):
            self.cursor.execute("INSERT INTO city (name, link, image, date) VALUES (%s, %s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), item['image'].encode('utf-8'), DATE))
            
        # Insert item into nordstrom table.
        elif isinstance(item, NordstromItem):
            self.cursor.execute("INSERT INTO nordstrom (name, link, image, date) VALUES (%s, %s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), item['image'].encode('utf-8'), DATE))
            
        # Insert item into barneys table.
        elif isinstance(item, BarneysItem):
            self.cursor.execute("INSERT INTO barneys (name, link, image, date) VALUES (%s, %s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), item['image'].encode('utf-8'), DATE))
            
        # Insert item into jimmyjazz table.
        elif isinstance(item, JimmyJazzItem):
            self.cursor.execute("INSERT INTO jimmyjazz (name, link, image, date) VALUES (%s, %s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), item['image'].encode('utf-8'), DATE))
            
        # Insert item into jdsports table.
        elif isinstance(item, JDSportsItem):
            self.cursor.execute("INSERT INTO jdsports (name, link, image, date) VALUES (%s, %s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), item['image'].encode('utf-8'), DATE))
            
        # Insert item into footpatrol table.
        elif isinstance(item, FootPatrolItem):
            self.cursor.execute("INSERT INTO footpatrol (name, link, image, date) VALUES (%s, %s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), item['image'].encode('utf-8'), DATE))
            
        # Insert item into sneakerbaas table.
        elif isinstance(item, SneakerBaasItem):
            self.cursor.execute("INSERT INTO sneakerbaas (name, link, image, date) VALUES (%s, %s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), item['image'].encode('utf-8'), DATE))
            
        # Insert item into sneakerpolitics table.
        elif isinstance(item, SneakerPoliticsItem):
            self.cursor.execute("INSERT INTO sneakerpolitics (name, link, image, date) VALUES (%s, %s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), item['image'].encode('utf-8'), DATE))
            
        # Insert item into urbanindustry table.
        elif isinstance(item, UrbanIndustryItem):
            self.cursor.execute("INSERT INTO urbanindustry (name, link, image, date) VALUES (%s, %s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), item['image'].encode('utf-8'), DATE))
            
        # Insert item into urbanoutfitters table.
        elif isinstance(item, UrbanOutfittersItem):
            self.cursor.execute("INSERT INTO urbanoutfitters (name, link, image, date) VALUES (%s, %s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), item['image'].encode('utf-8'), DATE))
            
        # Insert item into luisa table.
        elif isinstance(item, LuisaItem):
            self.cursor.execute("INSERT INTO luisa (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into slamjam table.
        elif isinstance(item, SlamJamItem):
            self.cursor.execute("INSERT INTO slamjam (name, link, image, date) VALUES (%s, %s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), item['image'].encode('utf-8'), DATE))
			
        # Insert item into rise45 table.
        elif isinstance(item, Rise45Item):
            self.cursor.execute("INSERT INTO rise45 (name, link, image, date) VALUES (%s, %s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), item['image'].encode('utf-8'), DATE))
			
        # Insert item into undefeated table.
        elif isinstance(item, UndefeatedItem):
            self.cursor.execute("INSERT INTO undefeated (name, link, image, date) VALUES (%s, %s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), item['image'].encode('utf-8'), DATE))
			
        # Insert item into zappos table.
        elif isinstance(item, ZapposItem):
            self.cursor.execute("INSERT INTO zappos (name, link, image, date) VALUES (%s, %s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), item['image'].encode('utf-8'), DATE))
			
        self.conn.commit()
		
        # If item name contain below words. Tweet it.
        if 'nmd' in item['name'].encode('utf-8').lower() or 'boost' in item['name'].encode('utf-8').lower() or 'retro' in item['name'].encode('utf-8').lower() or 'yeezy' in item['name'].encode('utf-8').lower():
          
          # Twitter Auth - Tweet the item with date, time, item name, and link.
          # To obtain Twitter CONSUMER and ACCESS keys go to https://apps.twitter.com/
          CONSUMER_KEY = ' PASTE CONSUMER_KEY HERE '
          CONSUMER_SECRET = ' PASTE CONSUMER_SECRET HERE '
          ACCESS_TOKEN_KEY = ' PASTE ACCESS_TOKEN_KEY HERE '
          ACCESS_TOKEN_SECRET = ' PASTE ACCESS_TOKEN_SECRET HERE '
          API = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
          TEXT_TO_TWEET = DATE + " EST " + item['name'] + " " + item['link']
          TWEET = API.request('statuses/update', {'status': TEXT_TO_TWEET})
          print(Fore.RED + 'LOG: SUCCESSFULLY TWEETED' + Style.RESET_ALL if TWEET.status_code == 200 else Fore.RED + 'LOG: FAILED TO TWEET' + Style.RESET_ALL)
          
    except MySQLdb.Error, e:
      print (Fore.RED + "ERROR %d: %s" % (e.args[0], e.args[1] + Style.RESET_ALL))
      
    return item
