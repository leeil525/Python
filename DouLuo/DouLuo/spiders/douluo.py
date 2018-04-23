# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
import re
from First.items import DouluoItem

class DouluoSpider(scrapy.Spider):
    name = 'douluo'
    allowed_domains = []
    start_urls = ['http://www.manhuatai.com/douluodalu/']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url,callback=self.parse,
                                args={'wait':1},endpoint='render.html')

    def parse(self, response):

        for url in response.xpath('//*[@id="topic1"]/li/a/@href').extract():
             url2 = 'http://www.manhuatai.com' + url
             yield SplashRequest(url=url2,callback=self.parse2,
                                args={'wait':1},endpoint='render.html')


    def parse2(self,response):

        page_number = re.search('totalimg:\d{1,2}', response.body).group(0)
        page_number = re.sub('\D', '', page_number)
        title=response.xpath('/html/body/div[2]/div[1]/h1/strong/text()').extract()[0]
        title=title.split(' ')[0]

        pct=response.xpath('//*[@id="comiclist"]/div[1]/img/@src').extract()[0]
        judge = pct.index('.jpg')
        for i in range(int(page_number)):
            Final = DouluoItem()
            url = pct[:judge - 1] + str(i + 1) + pct[judge:]
            Final['image_urls']=[url]
            Final['name']=title+'({0}).jpg'.format(str(i))
            yield Final





