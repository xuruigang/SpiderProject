# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem

class DmozSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domains = ['dmoztools.net']
    start_urls = ['http://www.dmoztools.net/Computers/Programming/Languages/Python/Books/',
                  'http://www.dmoztools.net/Computers/Programming/Languages/Python/Resources/'
    ]

    def parse(self, response):
        #  filename=response.url.split('/')[-2]+".html"
         # with open(filename, "wb") as fp:
          #    fp.write(response.body)
          
          divs=response.xpath('//*[@id="site-list-content"]/div/div[3]')
          for div in divs:
              item=TutorialItem()
              item['title']=div.xpath('a/div/text()').extract()
              item['link']=div.xpath('a/@href').extract()
              item['desc']=div.xpath('div/text()')[0].extract().strip()
              yield item
              
          
          
          
