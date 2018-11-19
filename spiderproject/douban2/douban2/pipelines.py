# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Douban2Pipeline(object):
    def process_item(self, item, spider):
        return item
class DoubanBookPipeline(object):
    def process_item(self, item, spider):
        info=item['content'].split('/')
        #[法] 圣埃克苏佩里 / 马振聘 / 人民文学出版社 / 2003-8 / 22.00元
        item['name'] = item['name']
        item['price'] = info[-1]
        item['edition_year'] = info[-2]
        item['publisher'] = info[-3]
        return item
