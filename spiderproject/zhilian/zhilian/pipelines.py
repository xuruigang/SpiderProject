# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

from zhilian.items import A51jobsItem


class ZhilianPipeline(object):
    def process_item(self, item, spider):
        return item
class A51jobsPipeline(object):
    def open_spider(self, spider):
         '''
         爬虫启动时出发该函数，spider为触发pipeline的爬虫实例
         '''
         self.__conn = pymysql.connect(
             host='127.0.0.1',
             port=3306,
             db='51jobs',
             user='root',
             passwd='root',
             charset='utf8')
         self.cu = self.__conn.cursor(pymysql.cursors.DictCursor)

         # self.m=MongoClient()#连接数据库
         # self.db=self.m.xiaoshuo#进入数据库
         # self.col=self.db[spider.name]#获取数据库
    def process_item(self, item, spider):
        if isinstance(item, A51jobsItem):
            # 查询学历id
            sql = '''select did from degree where dname=%s'''
            flag = self.cu.execute(sql, (item['degree'],))
            if flag:
                # 是否有重复数据
                degree_id = self.cu.fetchone()['did']
            else:
                sql = '''insert into degree(dname)values(%s)'''
                self.cu.execute(sql, (item['degree'],))
                self.__conn.commit()
                degree_id = self.cu.lastrowid
            # 查询职位
            sql = '''select pid from `position` where title=%s and degree_id=%s'''
            flag = self.cu.execute(sql, (item['title'], degree_id))
            if flag:
                position_id = self.cu.fetchone()['pid']
            else:
                sql = '''insert into `position`(title,salary,demand,numbers,`release`,degree_id)values(%s,%s,%s,%s,%s,%s)'''
                self.cu.execute(sql, (item['title'], item['salary'],item['demand'],item['numbers'],item['release'],degree_id))
                self.__conn.commit()
                position_id = self.cu.lastrowid
            # 存入数据库
            sql = '''select * from companys where position_id=%s'''
            flag = self.cu.execute(sql, (position_id,))
            if flag == 0:
                sql = '''insert into companys (cname,caddress,position_id)values(%s,%s,%s)'''
                self.cu.execute(sql, (item['company_name'], item['address'], position_id,))
                self.__conn.commit()
            return item

    def close_spider(self, spider):
        self.cu.close()
        self.__conn.close()