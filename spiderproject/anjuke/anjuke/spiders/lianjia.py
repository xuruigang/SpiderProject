# -*- coding: utf-8 -*-
import random
import time

import scrapy
from anjuke.items import LianjiaItem


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://xa.lianjia.com/zufang/']
    # sleep_time = random.randint(0, 2) + random.random()
    # print('开始休息：', sleep_time, '秒')
    # time.sleep(sleep_time)

    def parse(self, response):
        #links=response.css('#house-lst').css('a::attr("href")').extract()[1:]
        links=response.xpath('//*[@id="filter-options"]/dl[1]//a/@href').extract()[1:]
        for x in links:
            #利用response对象的urljoin方法补全url
            url=response.urljoin(x)
            yield scrapy.Request(url=url,callback=self.next1)

    def next1(self,response):
        #type_=response.xpath('//*[@id="filter-options"]/dl[1]/dd/div[1]/a[2]/text()').extract()
        #links=response.css('#house-lst').css('a::attr("href")').extract()
        links=response.xpath('//*[@id="house-lst"]/li//a/@href').extract()
        for url in links:
            yield scrapy.Request(url=url, callback=self.next2)

        next_=response.xpath('//div[4]/div[2]//a[7]/@href').extract()
        print(next_,'+++++++++++')
        if next_:
            yield scrapy.Request(url=response.urljoin(next_), callback=self.next1)

    # def next2(self, response):
    #     url = response.css('.orangeBtn::attr("href")').extract_first()
    #     image_urls = response.xpath('//*[@id="topImg"]/div[2]/ul/li/@data-src').extract()
    #     meta = {'number': 1, 'image_urls': image_urls}
    #     meta.update(response.meta)
    #     if url:
    #         yield scrapy.Request(url=response.urljoin(url), callback=self.next3, meta=meta)
    def next2(self,response):
        item=LianjiaItem()
        #item['type_'] = response.meta['type_']
        item['title']= response.xpath('//div[4]/div[1]/div/div[1]/h1').extract()
        item['community'] = response.xpath('//div[4]/div[2]/div[2]/div[2]/p[6]/a[1]/text()').extract()
        item['model'] = response.xpath('//div[4]/div[2]/div[2]/div[2]/p[2]/text()').extract()
        item['area'] = response.xpath('//div[4]/div[2]/div[2]/div[2]/p[1]/text()').extract()
        item['release_time'] = response.xpath('//div[4]/div[2]/div[2]/div[2]/p[8]/text()').extract()
        item['subway'] = response.xpath('//div[4]/div[2]/div[2]/div[2]/p[5]/text()').extract()
        item['price'] = response.xpath('//div[4]/div[2]/div[2]/div[1]/span').extract()
        item['position'] = response.xpath('//div[4]//div[2]/p[7]/a[1]/text()').extract()
        item['floor'] = response.xpath('//div[4]//div[2]/p[3]/text()').extract()
        item['broker']=response.xpath('//div[4]//div[3]//div[1]/a[1]/text()').extract()
        item['phones'] = response.xpath('//div[4]//div[3]//div[3]').extract()
        item['features'] = response.xpath('//*[@id="introduction"]//div[3]/ul//span[2]').extract()

        item['image_urls'] = response.xpath('//*[@id="topImg"]/div[2]/ul/li/@data-src').extract()
        yield item
