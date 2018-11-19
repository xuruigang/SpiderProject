# -*- coding: utf-8 -*-
import scrapy
from tianmao.items import TianmaoItem

class TmSpider(scrapy.Spider):
    name = 'tm'
    allowed_domains = ['www.tmall.com']
    start_urls = ['https://list.tmall.com/search_product.htm?q=%D5%EB%D6%AF%C9%C0&click_id=%D5%EB%D6%AF%C9%C0&from=mallfp..pc_1.0_hq&spm=875.7931836%2FB.a1z5h.1.66144265353lJ2']
    #记录处理的页数
    count=0
    def parse(self, response):
        TmSpider.count +=1
        divs = response.xpath('//div[@id="J_ItemList"]/div[@class="product"]/div')
        if not divs:#如果不存在打印日志
            self.log("list Page error--%s"%response.url)
        for div in divs:
            item=TianmaoItem()
            #商品价格
            item['goods_price']=div.xpath('p[@class="productPrice"]/em/@title')[0].extract()
            #商品名称
            item['goods_name'] = div.xpath('p[@class="productTitle"]/a/@title')[0].extract()
            #商品链接
            pre_goods_url=div.xpath("p[@class='productTitle]/a/@href")[0].extracrt()
            item['goods_url'] = pre_goods_url if 'http:' in pre_goods_url else ("http:"+pre_goods_url)
            #图片链接
            try:
                file_urls=div.xpath('div[@class="productImg-warp"]/a[1]/img/@src|'
                                   'div[@class="productImg-warp"]/a[1]/img/@data-ks-lazyload').extract()[0]
                item['file_urls'] = ["http:"+file_urls]
            except Exception as e:
                print('Error:',e)
                import pdb;pdb.set_trace()#显示错误路径
            yield scrapy.Request(url=item['goods_url'],meta={'item':item},callback=self.parse_detail,dont_filter=True)

    def parse_detail(self,response):
        div = response.xpath('//div[@class="extend"]/ul')
        if not div:
            self.log("Detail Page error--%s"%response.url)
        item=response.meta('item')
        div=div[0]
        #店铺名称
        item['shop_name']=div.xpath('li[1]/div/a/text()')[0].extract()
        #店铺链接
        item['shop_url'] = div.xpath('li[1]/div/a/@href')[0].extract()
        #公司名称
        item['company_name'] = div.xpath('li[3]/div/text()')[0].extract().strip()
        #公司地址
        item['company_url'] = div.xpath('li[4]/div/text()')[0].extract()

        yield item
