# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from qiancheng.items import QianchengItem


class QianchengPipeline(object):
    def process_item(self, item, spider):
        return item


class JobPipeline(object):
    def open_spider(self, spider):
        self.__conn = pymysql.connect(host="127.0.0.1", port=3306, db='qiancheng', user='root',
                                      password='root', charset='utf8')
        self.cu = self.__conn.cursor(pymysql.cursors.DictCursor)

    def process_item(self, item, spider):
        if isinstance(item, QianchengItem):
            # 查询文凭ID
            sql = 'select eid from education where education=%s'
            flag = self.cu.execute(sql, (item['education']),)
            if flag:
                education_id = self.cu.fetchone()['eid']
            else:
                sql = 'insert into education (education)values(%s)'
                self.cu.execute(sql, (item['education']))
                self.__conn.commit()
                education_id = self.cu.lastrowid
            # 查职称ID
            sql = 'select tid from title where title_name=%s and education_id=%s'
            flag = self.cu.execute(sql, (item['title_name'], education_id))
            if flag:
                title_id = self.cu.fetchone()['tid']
            else:
                sql = 'insert into title (title_name,money,time_,number_,education_id,suffer,url_ )' \
                      'values(%s,%s,%s,%s,%s,%s,%s)'

                self.cu.execute(sql, (item['title_name'], item['money'], item['time_'], item['number_'], education_id,
                                      item['suffer'], item['url_']))
                self.__conn.commit()
                title_id = self.cu.lastrowid
            # 存入数据库
            sql = 'select * from company where title_id=%s'
            flag = self.cu.execute(sql, (title_id,))
            if flag == 0:
                sql = 'insert into company (company_name, title_id, job_add)values(%s,%s,%s)'
                self.cu.execute(sql, (item['company_name'], title_id, item['job_add'],))
                self.__conn.commit()
            return item

    def close_spider(self, spider):
        self.cu.close()
        self.__conn.close()
