# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from cgi import log

import pymysql


class DoubanPipeline(object):
    def process_item(self, item, spider):
        print(item,"+++++++++")
        return item
class DoubanSqlPipeline(object):
    def __init__(self):
        #连接数据库
        self.connect = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            db='douban',
            user='root',
            passwd='root',
            charset='utf8',
            use_unicode=True
        )
        #通过cursor执行增删查改
        self.cursor=self.connect.cursor()
    def process_item(self, item, spider):
        try:
            # 查重处理
            self.cursor.execute(
                """select * from doubanmovie where move_name = %s""",
                   item['move_name'])
            # 是否有重复数据
            repetition = self.cursor.fetchone()

            # 重复
            if repetition:
                pass
            self.cursor.execute(
                """insert into  doubanmovie (serial_number, movie_name, introduce, star, evaluate, describes)value(%s, %s, %s, %s, %s, %s) """,
                (item['serial_number'],
                 item['movie_name'],
                 item['introduce'],
                 item['star'],
                 item['evaluate'],
                 item['describes']))
            # 提交sql语句
            self.connect.commit()
        except Exception as error:
                # 出现错误时打印错误日志
                log(error)
        return item
class MovePipeline(object):
    def process_item(self, item, spider):
        print(item,"+++++++++")
        return item