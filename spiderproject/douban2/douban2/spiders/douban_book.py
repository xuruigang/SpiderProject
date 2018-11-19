# -*- coding: utf-8 -*-
import scrapy
from douban2.items import DoubanBookItem

class DoubanBookSpider(scrapy.Spider):
    name = 'douban_book'
    allowed_domains = ['http://www.douban.com']
    start_urls = ['https://book.douban.com/top250']

    def parse(self, response):
        #请求第一页
        #yield scrapy.Request(response.url,callback=self.parse_next)
        #请求其它页
        links=response.xpath('//div[@class="paginator"]/a')
        for page in links:
            url=response.urljoin(page)
            yield scrapy.Request(url, callback=self.parse_next)
    def parse_next(self,response):
        for item in response.xpath('//tr[@class="item"]'):
            book = DoubanBookItem()
            book['name'] = item.xpath('td[2]/div/a/@title').extract()[0]
            book['author'] = item.xpath('td[2]/p[1]').extract()
            book['content'] = item.xpath('td[2]/p/text()').extract()[0]
            book['ratings'] = item.xpath('td[2]/div[2]/span[2]/text()').extract()[0]
            yield book
