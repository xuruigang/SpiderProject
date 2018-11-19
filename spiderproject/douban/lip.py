class LiepinSpider(scrapy.Spider):
    name = 'liepin'
    allowed_domains = ['www.liepin.com']
    start_urls = ['http://www.liepin.com/']

    headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
             'Accept-Encoding': 'gzip, deflate, br',
             'Accept-Language': 'zh-CN,zh;q=0.9',
             'Cache-Control': 'max-age=0',
             'Connection': 'keep-alive',
             'Host': 'www.liepin.com',
             'Upgrade-Insecure-Requests': 1,
             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
             }
    def parse(self, response):
        links=response.xpath('//*[@id="home"]/div[3]/div[2]/p/a/@href').extract()[0]
        for url in links:
            yield scrapy.Request(url=url,headers=self.headers,callback=self.next1)

    def next1(self,response):
        links=response.xpath('//*[@id="subsite"]//ul/li[1]/dl/dd/a/@href').extract()
        for x in links:
            url=response.urljoin(x)
            yield scrapy.Request(url=url,callback=self.next2)
    def next2(self,response):
        links=response.css(".sojob-list h3 a::attr('href')").extract()
        for y in links:
            url=response.urljoin(y)
            yield scrapy.Request(url=url,callback=self.next3)
        #next_ = response.css(".pagerbar a:nth-child(9)::attr('href')").extract()[0]
        next_ = response.xpath("//*[@id='sojob']/div[2]/div/div[1]/div[1]/div/div/a[8]/@href").extract()
        print(next_,'+++++++++++')
        if next_:
            yield scrapy.Request(url=response.urljoin(next_),callback=self.next2)
    def next3(self,response):
        item=LiepinItem()
        item['url']=response.xpath('//*[@class="title-info"]/h3/a/@href').extract()
        item['name'] = response.xpath('//*[@class="title-info"]/h1/text()').extract()
        item['company_name'] = response.xpath('//*[@class="title-info"]/h3/a/text()').extract()
        item['company_size'] = response.xpath('//*[@class="new-compintro"]/li[2]/text()').extract()
        item['company_address'] = response.xpath('//*[@class="new-compintro"]/li[3]/text()').extract()
        item['company_type'] = response.xpath('//*[@class="new-compintro"]/li[1]/a/text()').extract()
        item['pay'] = response.xpath('//*[@class="job-title-left"]/p[1]/text()').extract()
        item['publish_time'] = response.xpath('//*[@class="basic-infor"]//time/@title').extract()
        item['requires'] = response.xpath('//*[@class="job-qualifications"]/span/text()').extract()
        yield item



