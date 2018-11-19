# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from xici.settings import DBKWARGS


class XiciPipeline(object):
    def process_item(self, item, spider):
        DBKWARGS = spider.settings.get("DBKWARGS")
        con = pymysql.connect(**DBKWARGS)
        cur=con.cursor()
        sql = ("insert into proxy(IP,PORT,TYPES,POSITIONS,SPEED,LAST_CHECK_TIME)"
               "values(%s,%s,%s,%s,%s,%s)")
        lis = (item['IP'],item['PORT'],item['TYPES'],item['POSITIONS'],item['SPEED'],item['LAST_CHECK_TIME'])
        try:
            cur.execute(sql,lis)
        except Exception as e:
            print("插入错误：",e)
            con.rollback()
        else:
            con.commit()
        cur.close()
        con.close()
        return item
