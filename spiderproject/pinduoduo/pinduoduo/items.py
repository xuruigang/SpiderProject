# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PinduoduoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    goods_name = scrapy.Field()
    goods_price = scrapy.Field()
    normal_price = scrapy.Filed()
    sales = scrapy.Field()
    goods_id  = scrapy.Field()
    image_url = scrapy.Field()
    name = scrapy.Field()
