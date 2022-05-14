#!/usr/bin/env bash


[ ! "$(docker ps | grep splash)" ] && docker run -p 8050:8050 --net host scrapinghub/splash  2>&1 >/dev/null &

sleep 2

cd /home/dustin/github/roundTableSpider/
/usr/bin/scrapy crawl roundTable 2>&1 >/dev/null

mplayer -ao alsa -really-quiet -noconsolecontrols lirc=no ~/temp/roundtable_newest.mp3
# docker container kill $(docker container ls | grep splash | awk '{print $1}')

