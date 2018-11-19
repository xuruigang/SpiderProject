# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaoshuoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class XiaoshuoJobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name= scrapy.Field()#作者
    cation = scrapy.Field()#分类
    size = scrapy.Field()#大小
    progress = scrapy.Field()#进度
    upload = scrapy.Field()#上传会员
    update = scrapy.Field()#最后更新
    image_urls=scrapy.Field()
    images=scrapy.Field()

class MuluItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    types = scrapy.Field()
    book_name = scrapy.Field()
    images= scrapy.Field()
    image_urls = scrapy.Field()
    #catalogue =scrapy.Field()