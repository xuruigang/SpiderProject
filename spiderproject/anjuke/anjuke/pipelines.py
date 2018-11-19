# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import datetime
import os
import re
import sys


import datetime


import pymysql
from scrapy import Request



class LianjiaPipeline(object):
     def get_media_requests(self, item, info):
         # 循环每一张图片地址下载，若传过来的不是集合则无需循环直接yield
         for images in item['image_urls']:
             yield Request(images)
        #return item


class LiepinPipeline(object):
        def process_item(self, item, spider):
            print(item, "+++++++++")
            return item

class ZhiLianpeline(object):
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d')

    def __init__(self):
        if not os.path.exists('./zhaopin/'):
            os.mkdir('./zhaopin/')
        if not os.path.exists('./zhaopin/%szhaopin.csv' % self.nowTime):
            data = {'positionname': '职位',
                    'education': '学历',
                    'workLocation': '工作地点',
                    'company': '公司',
                    'salary': '薪水',
                    'publishTime': '职位',
                    'requirement': '要求', }
            self.saveContent(data)

    def saveContent(self, data):
        data = [data.get('positionname'), data.get('education'), data.get('workLocation'), data.get('publishTime'),
                data.get('salary'), data.get('company'), data.get('requirement')]
        csvfile = file('./zhaopin/%szhaopin.csv' % self.nowTime, 'ab')
        writer = csv.writer(csvfile)
        writer.writerow(data)
        csvfile.close()

    def process_item(self, item, spider):
        self.saveContent(item)
        return item




