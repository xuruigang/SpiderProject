# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QianchengItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title_name = scrapy.Field()
    company_name = scrapy.Field()
    education = scrapy.Field()
    money = scrapy.Field()
    job_add = scrapy.Field()
    time_ = scrapy.Field()
    number_ = scrapy.Field()
    suffer = scrapy.Field()  # 经验年限
    url_ = scrapy.Field()
