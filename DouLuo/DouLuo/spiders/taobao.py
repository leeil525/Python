# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class Spider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = []
    start_urls = ['https://s.taobao.com/search?q=%E7%BE%8E%E9%A3%9F']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse,
                                args={'wait': 1}, endpoint='render.html')

    def parse(self,response):
        titele = response.xpath('//div[@class="row row-2 title"]/a/text()').extract()
        print('这是标题：', titele)

