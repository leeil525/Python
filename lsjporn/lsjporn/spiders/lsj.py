# -*- coding: utf-8 -*-
import scrapy
import re
from lsjporn.items import LsjpornItem


class LsjSpider(scrapy.Spider):
    name = 'lsj'
    allowed_domains = ['*']
    start_urls = ['']
    def start_requests(self):
        for i in range(1,110):
            url='http://lsjporn.com/photo/all.html?page=' +  str(i)
            yield scrapy.Request(url,callback=self.parse)

    def parse(self, response):
        for pct,num in zip(response.xpath('//*[@id="container-main"]/div[2]/div/div/div[1]/a/img/@src').extract(),response.xpath('//*[@id="container-main"]/div[2]/div/div/div[1]/div/text()').extract()):
            num = int(re.sub('\D', '', num))
            for i in range(1,num+1):
                Lsj=LsjpornItem()
                Lsj['image_urls'] = [re.sub('\d{1,3}_m',str(i),pct)]
                yield Lsj


