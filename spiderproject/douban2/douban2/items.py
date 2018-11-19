# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Douban2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class DoubanBookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()  # 书名
    price = scrapy.Field()  # 价格
    edition_year = scrapy.Field()  # 出版年份
    publisher = scrapy.Field()  # 出版社
    ratings = scrapy.Field()  # 评分
    author = scrapy.Field()  # 作者
    content = scrapy.Field()

