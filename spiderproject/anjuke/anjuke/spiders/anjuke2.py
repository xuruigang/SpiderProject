# -*- coding: utf-8 -*-
import scrapy


class Anjuke2Spider(scrapy.Spider):
    name = 'anjuke2'
    allowed_domains = ['anjuke.com']
    start_urls = ['http://anjuke.com/']

    def parse(self, response):
        pass
