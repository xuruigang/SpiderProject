# -*- coding: utf-8 -*-
import scrapy
from zhilian.items import A51jobsItem


class A51jobsSpider(scrapy.Spider):
    name = '51jobs'
    #allowed_domains = ['51job.com']
    start_urls = ['https://search.51job.com/list/020000%252C010000%252C030200%252C040000%252C200200,000000,0107,01,9,99,%2520,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']

    def parse(self, response):
        links=response.css('.t1 span a::attr(href)').extract()
        for url in links:
            yield scrapy.Request(url=url,callback=self.next2)
        #next_ = response.css('.bk a::attr("href")').extract()
        next_ = response.css('.bk a::attr("href")').extract()[-1]
        if next_:
            yield scrapy.Request(url=next_,callback=self.parse)
    def next2(self,response):
        item=A51jobsItem()
        item['title'] = ''.join(response.css('h1::attr("title")').extract())
        item['company_name'] = ''.join(response.css('.catn::attr("title")').extract())
        item['salary'] = ''.join(response.css('h1~strong::text').extract())
        item['address'] = response.css('.msg::text').extract()[0].replace('\xa0\xa0','').strip()
        item['release'] = response.css('.msg::text').extract()[-1].replace('\xa0\xa0','').strip()
        #item['degree'] = response.css('.msg::text').extract()[2].replace('\xa0\xa0','').strip()
        item['degree'] =  response.xpath('//div[3]//div[2]/div/div[1]/p[2]/text()[3]').extract()[0].replace('\xa0\xa0','')
        item['numbers'] = response.css('.msg::text').extract()[3].replace('\xa0\xa0','').strip()
        item['demand'] = response.css('.msg::text').extract()[1].replace('\xa0\xa0','').strip()

        yield item
        # item['title']=  response.css('.cn h1::attr("title")').extract()
        # item['salary']= response.css('.cn strong::text')[0].extract().strip()
        # item['company_name'] = response.css('.cname a::attr("title")')[0].extract().strip()
        # item['address'] =  response.xpath("//div[3]//div[2]//div[1]/p[2]/text()[1]").extract()[0].strip()
        # item['demand'] =  response.xpath("//div[3]//div[2]//div[1]/p[2]/text()[2]").extract()[0].strip()
        # item['degree'] =  response.xpath("//div[3]//div[2]//div[1]/p[2]/text()[3]").extract()[0].strip()
        # item['numbers'] =  response.xpath("//div[3]//div[2]//div[1]/p[2]/text()[4]").extract()[0].strip()
        # #item['release'] = response.xpath("//div[3]//div[2]//div[1]/p[2]/text()[5]")[0].extract().strip()
        # item['url_'] = response.meta['url_']
        # item['release'] =  response.xpath("//div[3]//div[2]//div[1]/p[2]/text()[5]").extract()[0].strip()
        # yield item
        # item[''] =