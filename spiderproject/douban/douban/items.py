# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    serial_number = scrapy.Field()#序号
    movie_name = scrapy.Field()#名称
    introduce = scrapy.Field()#星级
    star = scrapy.Field()#电影介绍
    evaluate = scrapy.Field()#评论数
    describes = scrapy.Field()#描述
class MoveItem(scrapy.Item):
    # define the fields for your item here like
    #  name = scrapy.Field()
    directors = scrapy.Field()
    rate = scrapy.Field()
    cover_x = scrapy.Field()
    star = scrapy.Field()
    title = scrapy.Field()
    url= scrapy.Field()
    casts = scrapy.Field()
    cover_y=scrapy.Field()



class DoubanJobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # movie_name= scrapy.Field()#电影名称
    # director= scrapy.Field()#导演
    # starring = scrapy.Field()#主演
    # types = scrapy.Field()#类型
    # countries = scrapy.Field()#地区
    # language = scrapy.Field()#语言
    # release = scrapy.Field()#上映时间
    # introduction = scrapy.Field()#简介
    movie_name = scrapy.Field()
    movie_star = scrapy.Field()
    movie_quote = scrapy.Field()