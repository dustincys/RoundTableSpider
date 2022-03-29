#!/usr/bin/env bash

[ ! "$(docker ps | grep splash)" ] && docker run -p 8050:8050 scrapinghub/splash &

sleep 2

amixer set Master 100% unmute

cd /home/dustin/github/roundTableSpider/
/usr/bin/scrapy crawl roundTable 2>&1 >/dev/null

docker container kill $(docker container ls | grep splash | awk '{print $1}')

amixer set Master 0% mute
