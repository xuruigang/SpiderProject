# -*- coding: utf-8 -*-
import scrapy



class AmSpider(scrapy.Spider):
    name = 'am'
    #allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=mobile+phone&rh=i%3Aaps%2Ck%3Amobile+phone']
    

    def parse(self, response):
        print(response.url)
        titles=response.xpath('//ur[@id="s-results-list-atf"]/li//h2/text()').extract()
        hrefs=response.xpath('//ur[@id="s-results-list-atf"]/li//h2/../@href').extract()#../父级
        prices1=response.xpath('//ur[@id="s-results-list-atf"]/li//span[@class="sx-price-whole"]/text()').extract()
        prices1=response.xpath('//ur[@id="s-results-list-atf"]/li//sup[@class="sx-price-fractional"]/text()').extract()
        prices=[float('.'.join(item).replace(',', '')) for item in zip(prices1,prices2)]
        for item in zip(titles,hrefs,prices):
            yield{
                "title": item[0],
                "url": item[1],
                "prices": item[2]
                }
