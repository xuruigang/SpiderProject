# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChezhiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    number = scrapy.Field()
    brand = scrapy.Field()
    car_system = scrapy.Field()
    car_model = scrapy.Field()
    pro_brief = scrapy.Field()
    pro_description = scrapy.Field()
    time = scrapy.Field()
    status = scrapy.Field()
