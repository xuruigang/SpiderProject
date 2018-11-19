# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from xiaoshuo.items import MuluItem
from scrapy.loader import ItemLoader

class MuluSpider(CrawlSpider):
    name = 'mulu'
    allowed_domains = ['www.qidian.com']
    start_urls = ['http://www.qidian.com/all']

    rules = (
        Rule(LinkExtractor(allow=r'[a-zA-z]+://[^\s]*'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'.*'), follow=True),
    )

    def parse_item(self, response):
        i = ItemLoader(item=MuluItem(),response=response)
        i.add_css('types','.row-1 li:nth-child(2) a::text')
        i.add_css('book_name', '.book-mid-info h4 a::text')
        a=('http:')
        i.add_css('image_urls', '.book-img-box a img::attr("src")')
        # i['types']=response.css('.row-1 li:nth-child(2) a::text').extract()
        # i['book_name']=response.css('.book-mid-info h4 a::text').extract()
        # i['image_urls']=response.css('.book-img-box a img::attr("src")').extract()
        #i['catalogue']=response.css('.book-intro p::text').extract()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i.load_item()
