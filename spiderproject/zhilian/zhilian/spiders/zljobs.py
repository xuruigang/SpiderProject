# -*- coding: utf-8 -*-
import scrapy
from zhilian.items import ZhilianItem

class ZljobsSpider(scrapy.Spider):
    name = 'zlzp'
    allowed_domains = ['zhaopin.com']
    start_urls = [
        'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC%2B%E4%B8%8A%E6%B5%B7%2B%E5%B9%BF%E5%B7%9E%2B%E6%B7%B1%E5%9C%B3%2B%E6%AD%A6%E6%B1%89&kw=python&p=1&isadv=0',
        'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC%2B%E4%B8%8A%E6%B5%B7%2B%E5%B9%BF%E5%B7%9E%2B%E6%B7%B1%E5%9C%B3%2B%E6%AD%A6%E6%B1%89&kw=php&p=1&isadv=0',
        'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC%2B%E4%B8%8A%E6%B5%B7%2B%E5%B9%BF%E5%B7%9E%2B%E6%B7%B1%E5%9C%B3%2B%E6%AD%A6%E6%B1%89&kw=html&p=1&isadv=0'
    ]

    def parse(self, response):
        yield scrapy.Request(
            url=response.url,
            callback=self.parse_job_info,
            meta={},
            dont_filter=True,
        )

    def parse_job_info(self, response):
        """
            解析工作信息
        :param response:
        :return:
        """
        zl_table_list = response.xpath("//div[@id='newlist_list_content_table']/table[@class='newlist']")
        for zl_table in zl_table_list[1:]:
            # tbody 是网页自动生成的 运行起来看效果/或者右键查看源码
            # zl_td_list = zl_table.xpath("tr[1]/td")
            # 问题：td 数不是5个，会报错--索引越界
            # td1 = zl_table_list[0]
            # td2 = zl_table_list[1]
            # td3 = zl_table_list[2]
            # td4 = zl_table_list[3]
            # td5 = zl_table_list[4]

            # 查找元素尽量用xpath定位，少用索引，因为有可能出现索引越界错误
            # 只有在不明确错误时使用异常捕获
            # //text()获取标签内所有文本
            # extract()把列表里的元素转换成文本,本身还是列表
            # extract_first('默认值')把列表里的元素转换成文本并取出第一个，如果取不到，返回默认值
            td1 = zl_table.xpath("tr/td[@class='zwmc']/div/a//text()").extract()
            # map返回的是一个列表 td1 = list(map(str.strip, td1))
            td1 = map(str.strip, td1)
            job_name = "".join(td1).replace(",", "/")
            # strip()只能清除两端的
            fan_kui_lv = zl_table.xpath("tr/td[@class='fk_lv']/span/text()").extract_first('没有反馈率').strip()
            job_company_name = zl_table.xpath("tr/td[@class='gsmc']/a[1]/text()").extract_first('没有公司名称').strip()
            job_salary = zl_table.xpath("tr/td[@class='zwyx']/text()").extract_first('面议').strip()
            job_place = zl_table.xpath("tr/td[@class='gzdd']/text()").extract_first('没有工作地点').strip()
            print(job_name, fan_kui_lv, job_company_name, job_salary, job_place)
            item = ZhilianItem()
            item['job_name'] = job_name
            item['job_company_name'] = job_company_name
            item['job_place'] = job_place
            item['job_salary'] = job_salary
            item['job_time'] = "没有时间"
            item['job_type'] = "智联招聘"
            item['fan_kui_lv'] = fan_kui_lv
            yield item
        yield scrapy.Request(
            url=response.url,
            callback=self.parse_next_page,
            meta={},
            dont_filter=True,

        )

    def parse_next_page(self, response):
        """
            解析下一页
        :param response:
        :return:
        """
        #  //div[@class='pagesDown']/ul/li/a[text()='下一页']/@href
        next_page = response.xpath(" //a[text()='下一页']/@href").extract_first('没有下一页')
        if next_page:
            yield scrapy.Request(
                url=next_page,
                callback=self.parse_job_info,
                meta={},
                dont_filter=True,
            )
