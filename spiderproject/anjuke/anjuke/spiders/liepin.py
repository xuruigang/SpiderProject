# -*- coding: utf-8 -*-
import scrapy
from anjuke.items import LiepinItem
import scrapy
from anjuke.items import LiepinItem
#import main




# class LiepinSpider(scrapy.Spider):
#     name = 'liepin'
#     allowed_domains = ['www.liepin.com']
#     start_urls = ['http://www.liepin.com/']



class LiepinSpider(scrapy.Spider):
    name = 'liepin'
    allowed_domains = ['www.liepin.com']
    start_urls = ['https://www.liepin.com/it',]
    # 对请求的返回进行处理的配置
    # meta = {
    #     'dont_redirect': True,  # 禁止网页重定向
    #     'handle_httpstatus_list': [301, 302]  # 对哪些异常返回进行处理
    # }
    def parse(self, response):
        links=response.xpath('//*[@id="subsite"]//ul/li/dl/dd/a/@href').extract()
        for x in links:
            #print(x,"+++++++")
            url=response.urljoin(x)
            #print(url,"_______")
            yield scrapy.Request(url=url,callback=self.next2)
    def next2(self,response):
        links=response.css(".search-conditions  dl:nth-child(3) >dd a::attr('href')").extract()[1:5]
        for y in links:
            url=response.urljoin(y)
            yield scrapy.Request(url=url,callback=self.next3)
    def next3(self,response):
        links=response.css(".job-info h3 a::attr('href')").extract()
        for url in links:
            url = response.urljoin(url)
            yield scrapy.Request(url=url,callback=self.next4)
        next_ = response.css('.pagerbar a:nth-child(9)::attr("href")').extract_first()

        if next_:
            yield scrapy.Request(url=response.urljoin(next_), callback=self.next3)

    def next4(self,response):
        item=LiepinItem()
        #item['url']=response.xpath('//*[@class="title-info"]/h3/a/@href').extract()
        item['name'] = response.xpath('//*[@class="title-info"]/h1/text()').extract()
        item['company_name'] = response.xpath('//*[@class="title-info"]/h3/text()').extract()
        item['pay'] = response.xpath('//*[@class="job-title-left"]/p[1]/text()').extract()
        item['company_ads'] = response.xpath('//*[@id="job-view-enterprise"]//div[1]/div[2]//p[2]/span/a/text()').extract()
        item['degree'] = response.xpath('//*[@id="job-view-enterprise"]//div[2]/div[1]//div/span[1]').extract()
        item['experience'] = response.xpath('//*[@id="job-view-enterprise"]//div[2]/div[1]//div/span[2][0]').extract()
        item['ages'] = response.xpath('//*[@id="job-view-enterprise"]//div[2]/div[1]//div/span[4]').extract()
        item['publish_time'] = response.xpath('//*[@class="basic-infor"]//time/@title').extract()
        item['types']=response.xpath('//*[@id="job-view-enterprise"]//div/div[1]/div/ul/li[1]/a/text()').extract()
        yield item

