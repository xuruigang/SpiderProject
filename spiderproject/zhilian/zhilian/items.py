# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhilianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class A51jobsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()#职位
    salary = scrapy.Field()#薪资
    company_name = scrapy.Field()#公司名称
    address = scrapy.Field()#地址
    demand = scrapy.Field()#要求
    degree = scrapy.Field()#学历
    numbers = scrapy.Field()#人数
    release = scrapy.Field()#发布时间
    #url_=scrapy.Field()
    #name = scrapy.Field()
