# -*- coding: utf-8 -*-
import scrapy
from PIL import Image


class DbSpider(scrapy.Spider):
    name = 'db'
    allowed_domains = ['www.douban.com']
    start_urls = ['http://douban.com/']
    headers={
        'Accept':'text / html, application / xhtml + xm…plication / xml;q = 0.9*/*;q = 0.8',
        'Accept - Encoding':'gzip, deflate, br',
        'Accept - Language':'zh - CN, zh;q = 0.8, zh - TW;q = 0.7, zh - HK;q = 0.5, en - US;q = 0.3, en;q = 0.2',
        'Cache - Control':'max - age = 0',
        'Connection':'keep-alive',
        'Host':'accounts.douban.com',
        'Referer': 'https: // www.douban.com / accounts / login?source = main',
        'Upgrade - Insecure - Requests':1,
        'User - Agent':'Mozilla / 5.0(Windows NT 6.1;W…) Gecko / 20100101Firefox / 62.0'
    }
    #开整第二步，用爬虫获取验证码的ID，并调用函数获取验证图片
    def parse(self, response):
        captcha_no = response.xpath('//input[@name="captcha-id"]/@value').extract_first()
        # 'WwiHNP3kMmpKs6CkDTeTEfDN:en'
        # ySVwKvFAdD6NZiNXCegXCF37: en
        # https: // www.douban.com / misc / captcha?id = lkxyg9TMwrzPrmwDUl3iNLnG:en & size = s
        captcha_url = 'https://www.douban.com/misc/captcha?id=%s&size = s' % captcha_no
        yield scrapy.Request(url=captcha_url, method='GET', callback=self.do_captcha_before_login, headers=self.headers,
                             meta={'captcha_no': captcha_no})

    #第三步：输入验证码，并设置formdata，提交表单并登录
    def do_captcha_before_login(self, response):
        captcha_no = response.meta['captcha_no']
        # print(response.body)
        with open('captcha.gif', 'wb') as f:
            f.write(response.body)
            f.close()
        try:
            im = Image.open('captcha.gif')
            im.show()
            im.close()
        except:
            pass
        # 根据打开的图片输入验证吗
        captchaStr = input('请输入验证码:')
        print(captchaStr)
        login_url = 'https://accounts.douban.com/login'
        login_data = {
            'source': 'index_nav',
            'redir': 'https://www.douban.com/',
            'form_email': '18740430682',
            'form_password': '############',
            'captcha-solution': captchaStr,
            'captcha-id': captcha_no,
            'login': '登录'
        }
        yield scrapy.FormRequest(url=login_url, formdata=login_data, headers=self.headers,
                                 callback=self.parse_login_after)
    #第四步：登录后
    def parse_login_after(self, response):
        txlist = response.xpath('//*[@class="status-item"]/div/div[1]/div[2]/a/text()').extract()
        for tx in txlist:
            print(tx)
