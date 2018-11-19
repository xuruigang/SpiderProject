#!/usr/bin/python3
#coding=utf-8
import redis, pickle, os, gzip
#pickle用于python特有的类型和python的数据类型间进行转换
#pickle提供四个功能：dumps,dump,loads,load
from bs4 import BeautifulSoup
from chardet import detect
from urllib import request, parse
from fake_useragent import UserAgent
# 代理池
class ProxyPool(object):
    '''
    IP代理池
    该代理池地址由https://www.kuaidaili.com免费提供
    '''

    def __init__(self, max=5, check_url='http://www.baidu.com'):
        '''
        代理对象初始化时需要参数如下：
        @max 为代理池的大小
        @check_url 为代理池的检测地址【可选】默认为http://www.baidu.com
        设计思路：
        默认可以将本次的代理信息进行保存，一般在当前对象所在目录下的poxy.pickle文件中
        '''
        self.__max = max
        self.__check_url = check_url
        self.__proxy_get_url = 'https://www.kuaidaili.com/free/'
        self.__get_proxy()  # 初始化代理池

    def __get_proxy(self):
        '''
        初始化代理池地址
        '''
        if os.path.isfile('./poxy.pickle'):#使用os.path.isfile()函数判断某一路径是否为文件
            with open('./poxy.pickle', 'rb') as f:#以二进制模式读取文件
                self.__Pool = pickle.load(f)
        else:
            self.__Pool = set()#代理池是一个空的集合
        self.get_chack_pool()  # 检查并获取真实的代理池内容

    def get_chack_pool(self):
        '''
        检查并完整代理池
        '''
        proxys = set()#代理等于一个空的集合
        for proxy in self.__Pool:#proxy依次表示代理池中的一个元素，遍历完所有元素循环结束
            if self.__check(proxy):#如果检查代理可用，就添加到集合中
                proxys.add(proxy)
        self.__Pool = proxys
        if len(self.__Pool) < self.__max:#如果长度小于最大长度，就补全代理
            self.__crawl_proxy()

    def __check(self, proxy):
        '''
        代理检查方法
        '''
        if isinstance(proxy, str):#isinstance() 函数来判断一个对象是否是一个已知的类型（对象，类型）
            proxy = eval(proxy)#proxy将字符串str当成有效的表达式来求值并返回计算结果
        proxy_handler = request.ProxyHandler(proxy)  # 创建代理对象
        opener = request.build_opener(proxy_handler)#创建ProxyHandler实例，并将实例作为build_opener()的参数
        try:
            req = opener.open(self.__check_url)#build_opener ()返回的对象具有open()方法，打开代理
        except:
            return False
        if req.status == 200:
            return True
        else:
            return False

    def __crawl_proxy(self):
        '''
        代理补全抓取方法
        '''
        pool = set()
        while True:
            proxys = self.get_proxy()#获取代理网站的代理地址赋给变量proxys
            for proxy in proxys:
                if self.__check(proxy):
                    pool.add(proxy)#代理池中添加代理
            if len(pool) < self.__max - len(self.__Pool):
                continue
            else:
                for proxy in pool:
                    self.__Pool.add(proxy)
                # 代理池回写 以备下次使用
                with open('./poxy.pickle', 'wb') as f:
                    pickle.dump(self.__Pool, f)
                break

    def get_proxy(self):
        '''
        获取代理网站的代理地址
        '''
        rep = request.urlopen(self.__proxy_get_url)
        #调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示
        data = rep.read()
        if 'gzip' in rep.getheader('Content-Encoding'):
            data = gzip.decompress(data)#解压后获取字节数据
        html = data.decode(detect(data)['encoding'], errors='ignore')
        #errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略
        sel = BeautifulSoup(html, 'html.parser')
        proxys = set()
        items = sel.find(name='tbody').find_all(name='tr')
        for x in items:
            s = x.find_all(name='td')
            item = {}
            key = s[3].string
            value = key + '://' + s[0].string + ':' + s[1].string
            item[key] = value
            item = str(item)
            if item not in self.__Pool:
                proxys.add(item)
        try:
            if rep.url == 'https://www.kuaidaili.com/free/':
                self.__proxy_get_url = 'https://www.kuaidaili.com/free/inha/2/'
            else:
                n = rep.url.split('/')[-2]#split()通过指定分隔符对字符串进行切片，如果参数num 有指定值，则仅分隔 num 个子字符串
                n = int(n) + 1
        except:
                self.__proxy_get_url = 'https://www.kuaidaili.com/free/inha/' + str(n) + '/'
        return proxys

    def getProxy(self):
        data = self.__Pool.pop()#移除代理池中的一个元素（默认最后一个元素），并且返回该元素的值
        self.__Pool.add(data)#再添加一个
        return eval(data)
if __name__ == "__main__":
     proxy=ProxyPool()
     print(proxy.getProxy())