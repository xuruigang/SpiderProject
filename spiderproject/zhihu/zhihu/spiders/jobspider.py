# -*- coding: utf-8 -*-
import scrapy


class JobspiderSpider(scrapy.Spider):
    name = 'jobspider'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    def parse(self, response):
        pass
