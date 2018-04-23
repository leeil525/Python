# -*- coding: utf-8 -*-
import scrapy
from First.items import NewsItem

class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['*']
    start_urls = ['http://news.qq.com/']

    def parse(self, response):
        href=response.xpath('/html/body/div[6]/div[2]/div[1]/div[1]/div/div/div/em/a/@href').extract()
        text=response.xpath('/html/body/div[6]/div[2]/div[1]/div[1]/div/div/div/em/a/text()').extract()
        for sel,fo in zip(href,text):

            item=NewsItem()
            item['url']=sel
            item['title'] = fo#sel.xpath('a/text()').extract()[0]
            yield item
            yield scrapy.Request(sel, callback=self.parse_content,dont_filter=True)

    def parse_content(self,response):
        item=NewsItem()
        item['content']=response.xpath('/html/head/meta[1]/@content').extract()
        item['time']=response.xpath('/html/head/meta[3]/@content').extract()
    #     with open('a.txt', 'a+') as file:
    #         file.write(response.xpath('/html/head/meta[1]/@content').extract()[0])
        yield item

