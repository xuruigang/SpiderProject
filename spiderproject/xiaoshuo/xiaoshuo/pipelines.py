# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from xiaoshuo.items import XiaoshuoJobItem
from pymongo import MongoClient
import pymysql
class MuluPipeline(object):
    def process_item(self, item, spider):
        print(item,'+++++++++++++')
        return item

class XiaoSqlPipeline(object):
    def open_spider(self,spider):
        '''
        爬虫启动时出发该函数，spider为触发pipeline的爬虫实例
        '''
        self.__conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            db='xiaoshuo1',
            user='root',
            passwd='root',
            charset='utf8')
        self.cu=self.__conn.cursor(pymysql.cursors.DictCursor)

        # self.m=MongoClient()#连接数据库
        # self.db=self.m.xiaoshuo#进入数据库
        # self.col=self.db[spider.name]#获取数据库
    def process_item(self,item,spider):
        '''
        当爬虫刨除一个item实例是触发该函数向该方法传入触发的item实例及爬虫实例
        '''
        #当传入的item为XiaoshuoJobItem类型时将其转换为字典存入MongoDB
        # if isinstance(item,XiaoshuoJobItem):
        #     self.col.insert_one(dict(item))
        # #将item返回以带后继的pipeline进行处理
        # return item
        if isinstance(item, XiaoshuoJobItem):
            #查询分类
            sql = 'select * from book where name=%s'
            flag = self.cu.execute(sql,(item['name'],))
            if flag:
                tid=self.cu.fetchone()
            else:
                sql='insert into book(name,cation,size,progress,upload,update,image_urls)values(%s,%s,%s,%s,%s,%s,%s)'
                self.cu.execute(sql,(item['name'],item['cation'],item['size'],item['progress'],item['upload'],item['update'],item['image_urls']))
                self.__conn.commit()
                tid=self.cu.lastrowid
            return item

def close_spider(self,spider):
        '''
        当爬虫关闭时触发该方法，一般可以用来数据库的断开操作
        '''
        self.m.close()
