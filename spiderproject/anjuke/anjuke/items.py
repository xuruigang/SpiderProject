# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AnjukeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()# 标签
    #type_=scrapy.Field()#分类
    community = scrapy.Field()# 小区
    model = scrapy.Field()#户型
    area = scrapy.Field()#面积
    release_time = scrapy.Field()#发布时间
    subway = scrapy.Field()#地铁
    price = scrapy.Field()#价格
    position = scrapy.Field()#位置
    floor = scrapy.Field()#楼层
    #imges=scrapy.Field()
    broker = scrapy.Field()#经纪人
    phones = scrapy.Field()#电话
    features = scrapy.Field() #特征
    image_urls = scrapy.Field()
class LiepinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #url = scrapy.Field()#链接
    name = scrapy.Field()#职位名称
    company_name = scrapy.Field()#公司名称
    pay = scrapy.Field()#薪资
    company_ads = scrapy.Field()#地址
    degree = scrapy.Field()#学历
    experience = scrapy.Field()#经验
    ages = scrapy.Field()#年龄
    publish_time = scrapy.Field()#发布时间
    types=scrapy.Field()#类型
class ZhiLianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #url = scrapy.Field()#链接
    # 职位名
    positionname = scrapy.Field()
    # 学历
    education = scrapy.Field()
    # 工作地点
    workLocation = scrapy.Field()
    # 发布时间
    publishTime = scrapy.Field()
    # 工资
    salary = scrapy.Field()
    # 公司名
    company = scrapy.Field()
    # 要求
    requirement = scrapy.Field()
