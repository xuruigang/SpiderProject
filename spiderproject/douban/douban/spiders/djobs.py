# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from douban.items import DoubanItem


class DjobsSpider(scrapy.Spider):
    name = 'djobs'#爬虫名
    allowed_domains = ['movie.douban.com']#允许的域名
    start_urls = ['https://movie.douban.com/top250']#入口url扔到调度器里面
    #默认解析方法
    def parse(self, response):
        #循环电影条目
        movie_list=response.xpath('//div[@class="article"]//ol[@class="grid_view"]/li')
        for i_item in movie_list:
            #item文件导进来
            douban_item=DoubanItem()
            #写详细的xpath，进行数据的解析
            douban_item['serial_number']=i_item.xpath(".//div[@class='item']//em/text()").extract_first()#extract_first解析第一个数据
            #.在当前xpath下细分
            douban_item['movie_name'] = i_item.xpath(".//div[@class='info']/div[@class='hd']/a/span[1]/text()").extract_first()
            content = i_item.xpath(".//div[@class='info']/div[@class='bd']/p[1]/text()").extract()
            #数据的处理
            for i_content in content:
                content_s="".join(i_content.split())
                douban_item['introduce']=content_s
            douban_item['star'] = i_item.xpath(".//span[@class='rating_num']/text()").extract_first()
            douban_item['evaluate'] = i_item.xpath(".//div[@class='star']//span[4]/text()").extract_first()
            douban_item['describes'] = i_item.xpath(".//p[@class='quote']/span/text()").extract_first()
            yield douban_item#把第一页的数据yield到管道pipline里面去 pipline接收数据,进行数据清洗，储存
        #解析下一页规则，取的后页的xpath
        next_link=response.xpath('//span[@class="next"]/link/@href').extract()#下一页
        print(next_link)
        if next_link:
            next_link=next_link[0]#有链接就去，没有就不取
            yield scrapy.Request("https://movie.douban.com/top250"+next_link,callback=self.parse)
        # for movie in movies:
        #     movie_name = movie.xpath('div[@class="hd"]/a/span/text()').extract()
        #     movie_star = movie.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()
        #     movie_quote = movie.xpath('div[@class="bd"]/p[@class="quote"]/span[@class="inq"]/text()').extract()
        #     print(movie_name)
        #     print(movie_star)
        #     print(movie_quote)
        #     item = DoubanJobItem()
        #     item['movie_name'] = movie_name
        #     item['movie_star'] = movie_star
        #     item['movie_quote'] = movie_quote
        #     yield item
        #     print(movie_name)
        #     print(movie_star)
        #     print(movie_quote)


