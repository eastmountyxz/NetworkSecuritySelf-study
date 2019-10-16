# -*- coding:utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup as bs
import telnetlib

#爬取数据
def proxy_spider():
    #设置请求
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
    url = 'https://www.xicidaili.com/nn'
    r = requests.get(url=url, headers=headers)
    print r

    #解析 通过re.compile('|[^odd]')解析奇数和偶数行
    soup = bs(r.content, 'lxml')
    datas = soup.find_all(name='tr', attrs={'class': re.compile('|[^odd]')})
    
    for data in datas:
        soup_proxy_content = bs(str(data), 'lxml')
        soup_proxys = soup_proxy_content.find_all(name='td')
        ip = str(soup_proxys[1].string)
        port = str(soup_proxys[2].string)
        types = str(soup_proxys[5].string)
        #print ip, port, types
        
        #判断IP地址是否存活
        proxy = {}
        proxy[types.lower()] = '%s:%s' % (ip, port)
        #proxy_check(ip, port, types)
        proxy_telnet(ip, port, types)

#获取能成功使用的代理ip内容 调用requests代理访问方法
def proxy_check(ip, port, types):
    proxy = {}
    proxy[types.lower()] = '%s:%s' % (ip, port)
    #proxy = {'http':'119.254.84.90:80'}
    try:
        r = requests.get('http://1212.ip138.com/ic.asp', proxies=proxy, timeout=6)
        #print r.text
        ip_content = re.findall(r"\[(.*?)\]", r.text)[0]
        if ip == ip_content:
            print proxy
    except Exception, e:
        print e
        pass

#检测IP地址是否存活
def proxy_telnet(ip, port, types):
    proxy = {}
    proxy[types.lower()] = '%s:%s' % (ip, port)
    
    try:
        telnetlib.Telnet(ip, port, timeout=2)
        print 'True:', proxy
    except:
        print 'False:', proxy
    
proxy_spider()
