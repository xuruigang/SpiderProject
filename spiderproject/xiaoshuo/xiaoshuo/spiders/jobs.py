# -*- coding: utf-8 -*-
import scrapy
from  xiaoshuo.items import XiaoshuoJobItem

class JobsSpider(scrapy.Spider):
    name = 'jobs'#爬虫名
    allowed_domains = ['www.jjxsw.com']
    start_urls = ['http://www.jjxsw.com/']

    def parse(self, response):
        links=response.css('#rate > dl > dd > li a::attr("href")').extract()
        for x in links:
            #利用response对象的urljoin方法补全url
            url=response.urljoin(x)
            yield scrapy.Request(url=url,callback=self.contents)
    def contents(self,rp):
        item=XiaoshuoJobItem()
        item['name'] = rp.css('.zuozhe a::text').extract()
        item['cation'] = rp.css('.downInfoRowL li::text').extract()[0]
        item['size'] = rp.css('.downInfoRowL li::text').extract()[1]
        item['progress'] = rp.css('.downInfoRowL>li span::text').extract()
        item['upload'] = rp.css('.downInfoRowL > li:nth-child(8) > a::text').extract()
        item['update'] = rp.css('.downInfoRowL li::text').extract()[4]
        item['image_urls']=rp.css('.img img::attr(src)').extract()
        yield item
