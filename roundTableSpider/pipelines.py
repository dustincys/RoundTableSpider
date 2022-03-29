# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import vlc
import time
from subprocess import call
from itemadapter import ItemAdapter

class RoundtablespiderPipeline:
    def process_item(self, item, spider):
        print('item["link"]')
        print(item["link"])
        call(["mplayer", '-ao', 'alsa', '-really-quiet', '-noconsolecontrols', "lirc=no", item["link"]])
        return item
