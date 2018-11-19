# -*- coding: utf-8 -*-
import scrapy
from chezhi.items import ChezhiItem
from chezhi.cTypeInfo import *
import random


class ChezhiSpider(scrapy.Spider):
    name = 'chezhi02'
    #allowed_domains = ['12365auto.com']
    start_urls = ['http://www.12365auto.com/']

    def start_requests(self):
        reqs=[]#定义一个空列表，收集所有的响应
        for i in range(1,7196):
            url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-%s.shtml'%i
            req=scrapy.Request(url,callback=self.parse)
            reqs.append(req)
        return reqs


    def parse(self, response):
        global car_exception_dic #声明一个全局变量
        tclass = response.xpath('//*[@id="content"]/div[4]/div[2]/table')
        print(tclass)
        trs=tclass.xpath('//tr')[1:]
        print(trs)#去除标题列
        items=[]
        for tr in trs:
            print(tr)
            pre_item=ChezhiItem()
            pre_item['number']=tr.xpath('//tr[2]/td[1]/text()').extract_first()
            pre_item['brand'] = tr.xpath('//tr[2]/td[2]/text()').extract_first()
            pre_item['car_system'] = tr.xpath('//tr[2]/td[3]/text()').extract_first()
            pre_item['car_model'] = tr.xpath('//tr[2]/td[4]/text()').extract_first()
            pre_item['pro_brief'] = tr.xpath('//tr[2]/td[5]/a/text()').extract_first()
            ex_type_str=tr.xpath('//tr[2]/td[6][@class="tsgztj"]/text()').extract_first()
            pre_item['pro_description']=''.join([car_exception_dic[ex_type] for ex_type in ex_type_str.split(',') if ex_type])#根据cTypeInfo获取对应信息
            print(pre_item['pro_description'])
            pre_item['time'] = tr.xpath('//tr[2]/td[7]/text()').extract_first()
            pre_item['status'] = tr.xpath('//tr[2]/td[8]/em/text()').extract_first()
            items.append(pre_item)
        return items
