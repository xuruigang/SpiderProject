# -*- coding: utf-8 -*-
import scrapy
from movie.items import MovieItem

class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    #allowed_domains = ['meijutt.com']
    start_urls = ['meijutt.com/new100.html']

    def parse(self, response):
        movies=response.xpath('//ul[@class="top-list  fn-clear"]/li')
        for each_move in movies:
            item=MovieItem()
            item['name']=each_move.xpath('./h5/a/@title').extract()[0]
            yield item

