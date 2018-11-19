# -*- coding: utf-8 -*-
import scrapy
import re
import json
from douban.items import MoveItem


class MySpider(scrapy.Spider):
    name = 'douban_ajax'
    #allowed_domains = ['douban.com']
    #start_urls = ['https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start=0']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url='https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start=0'
        yield scrapy.Request(url=url,headers=self.headers)
    def parse(self, response):
        datas = json.loads(response.body)
        item=MoveItem()
        if datas:
            for data in datas:
                print(datas)
                item['directors']=data['directors']
                item['rate'] = data['rate']
                item['cover_x'] = data['cover_x']
                item['star'] = data['star']
                item['title'] = data['title']
                item['url'] = data['url']
                item['casts'] = data['casts']
                item['cover_y'] = data['cover_y']
                # 如果datas存在数据则对下一页进行采集
                page_num = re.search(r'start=(\d+)', response.url).group(1)
                page_num = 'start=' + str(int(page_num) + 20)
                next_url = re.sub(r'start=\d+', page_num, response.url)
                yield scrapy.Request(next_url, headers=self.headers)




