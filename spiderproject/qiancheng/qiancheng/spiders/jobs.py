# -*- coding: utf-8 -*-
import scrapy




import scrapy
from qiancheng.items import QianchengItem

class JobSpider(scrapy.Spider):
    name = 'job'
    # allowed_domains = ['www.51job.com']
    start_urls = ['https://search.51job.com/list/020000%252C010000%252C030200%252C040000%252C200200,000000,0107,01,9,99,%2520,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']

    def parse(self, response):
        links = response.css('.t1 span a::attr(href)').extract()
        for url in links:
            meta = {'url_': url}
            meta.update(response.meta)
            yield scrapy.Request(url=url, callback=self.next, meta=meta)
        next_ = response.css('.bk a::attr(href)').extract()[-1]
        if next_:
            yield scrapy.Request(url=next_, callback=self.parse)

    def next(self, response):
        item = QianchengItem()
        item['title_name'] = ''.join(response.css('h1::attr(title)').extract())
        item['company_name'] = ''.join(response.css('.catn::attr(title)').extract())
        item['money'] = ''.join(response.css('h1~strong::text').extract())
        item['job_add'] = ''.join(response.css('.msg::text').extract()[0]).replace('\xa0\xa0','').strip()
        item['time_'] = ''.join(response.css('.msg::text').extract()[-1]).replace('\xa0\xa0','').strip()
        test_education = '初中及以下高中中技中专大专本科硕士博士'
        item['education'] = ''.join(response.css('.msg::text').extract()[2]).replace('\xa0\xa0','').strip()
        if item['education'] not in test_education:
            item['education'] = '不限'
        item['number_'] = ''.join(response.css('.msg::text').extract()[3]).replace('\xa0\xa0','').strip()
        item['suffer'] = ''.join(response.css('.msg::text').extract()[1]).replace('\xa0\xa0','').strip()
        item['url_'] = response.meta['url_']

        yield item

