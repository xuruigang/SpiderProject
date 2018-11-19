# -*- coding: utf-8 -*-
import scrapy
import json
from pinduoduo.items import PinduoduoItem

class PddSpider(scrapy.Spider):
    name = 'pdd'
    allowed_domains = ['yangkeduo.com']
    page=1
    start_urls = [''http://apiv3.yangkeduo.com/v5/goods?page=' + str(page) + '&size=400&column=1&platform=1&assist_allowed=1&list_id=single_jXnr6K&pdduid=0']
    '']

    def parse(self, response):
        goods_list_json = json.loads(response.body)
        goods_list=goods_list_json['goods_list']
        if not goods_list:
            return
        for goods in goods_list:
            item=PinduoduoItem()
            item['goods_name']=goods['goods_name']
            item['goods_price']=float(goods['group']['price']) / 100
            item['sales'] = goods['cnt']
            item['normal_price']=float(goods['normal_price']) / 100
            item['goods_id']=goods['goods_id']
            yield scrapy.Request(url='http://apiv3.yangkeduo.com/reviews/" + str(item['goods_id']) + "/list?&size=20",
                                 callback=self.get_comments, meta={"item": item}')

        self.page += 1
        yield scrapy.Request(url='http://apiv3.yangkeduo.com/v5/goods?page=' + str(self.page) + '&size=400&column=1&platform=1&assist_allowed=1&list_id=single_jXnr6K&pdduid=0',
                             callback=self.parse)
    def get_comment(self, response):
            item=response.meta['item']
            comment_list_json = json.load(response.body)
            comment_list = json.loads['data']
            comments = []
            for comment in comment_list:
                 if comment['comment'] == '':
                                 continue
                 comments.append(comment['comment'])
            item['comments'] = comments
                                 
                                 

            
