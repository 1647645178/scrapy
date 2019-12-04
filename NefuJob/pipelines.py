# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import re
c=re.compile(r'\'(.*?)\'')

class NefujobPipeline(object):
    def process_item(self, item, spider):
        return item
class MathJobInfoPipeline(object):
    def open_spider(self, spider):
        self.f = open('Info.txt', 'a')
 
    def close_spider(self, spider):
        self.f.close()
 
    def process_item(self, item, spider):
        if item!=None:
            self.f.write(':'.join(c.findall(str(item)))+'\n')
