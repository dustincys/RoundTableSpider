import scrapy
import re
from roundTableSpider.items import RoundtablespiderItem
from scrapy_splash import SplashRequest

class RoundtableSpider(scrapy.Spider):
    name = 'roundTable'
    allowed_domains = ['http://ezfm.cri.cn']
    start_urls = ['http://ezfm.cri.cn/columnList/ezfm/11/']

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'DNT': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Chrome/78.0.3904.87',
        'Sec-Fetch-User': '?1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;zen-US,en;q=0.9'
    }

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url,
                                args={'wait': 5})

    def parse(self, response):
        self.logger.info("found html:")
        self.logger.info(response.css("html").getall())
        eventObjs = response.xpath("/html/body/div[1]/div[2]/div/div[1]/div[4]/ul//i").getall()
        self.logger.info("eventObjs[0]:")
        self.logger.info(eventObjs[0])

        eventText = eventObjs[0]

        dataUrl = re.search("(?<=data-url=\").+?(?=\")", eventText).group()
        dataDate = re.search("(?<=data-date=\").+?(?=\")", eventText).group()
        dataTitle = re.search("(?<=data-title=\").+?(?=\")", eventText).group()

        self.logger.info(dataUrl)
        self.logger.info(dataDate)
        self.logger.info(dataTitle)

        rItem = RoundtablespiderItem()
        rItem['title'] = dataTitle
        rItem['time'] = dataDate
        rItem['link'] = dataUrl

        yield rItem
        pass
