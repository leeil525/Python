# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline

class DownImagePipeline(ImagesPipeline):
    def get_media_requests(self,item,info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url,meta={'item':item})
    def file_path(self,request,response=None,info=None):
        item=request.meta['item']
        filename=u"{0}".format(item['name'])
        return filename




class FirstPipeline(object):
    def process_item(self, item, spider):
        return item






