# -*- coding:utf-8 -*-
import requests
from  bs4 import BeautifulSoup
import cookielib
import re
# -*- new -*-
# -*- 模拟登陆 changl-*-
# -*- 获取网页 -*-
headers={
     'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0",
     'Cookie':"locale=zh-CN; _fofapro_ars_session=f3aad5f0371d29018f3b0f0a1895ade8",
}
r = requests.get ('https://fofa.so/result?q=domian="qq.com"', headers=headers)
r.encoding='utf-8'

# -*- 把网页存入soup -*-
soup = BeautifulSoup(r.text,'html.parser')

# -*-t提取标题print soup.title.text -*-
# -*- 端口       port= news.select('.list_mod_t .span  ')[0].text    -*-
# -*- 名字,IP 等信息        for l i in news.select('.list_mod_c li  '):     print li.text.strip()     -*-
# -*- 能获取li不同的东西 print news.select('.list_mod_c li  ')[4].text -*-

# -*- 端口的指纹信息       print news.select('.list_mod_c  .auto-wrap')[0].text    -*-
#z这个用来判断是否是IP
for news in soup.select('.list_mod'):
    lis=news.select('.list_mod_c li  ')
    for i in {0,1,2,3}:
        m=lis[i].text.strip()
        if re.match(r'^2016[0-9-]*',m):
             time=re.match(r'^20[0-9-]*',m).group()
             print 'time:'+time
        elif re.match(r'^[0-9]*.[0-9]*.[0-9]*.[0-9]*$',m):
             ip=re.match(r'^[0-9]*.[0-9]*.[0-9]*.[0-9]*$',m).group()
             print 'ip:'+ip
        else:
             print 'operaton=NULL'

    for i in {3,4}:
        m=lis[i].text.strip()
        if re.match(r'[a-zA-Z\s/]*',m):
            location=re.match(r'[a-zA-Z\s/]*',m).group()
            print 'location:'+location
        break;

    for i in {4,5}:
        m=lis[i].text.strip()
        if re.match(r'[\w.]*[.com|.cn]$|^[0-9]*.[0-9]*.[0-9]*.[0-9]*$',m):
            domian=re.match(r'[\w.]*[.com|.cn]$|^[0-9]*.[0-9]*.[0-9]*.[0-9]*$',m).group()
            print 'domian:'+domian
            break;
        else:
            print 'domian=NULL'
    for i in {5,6}:
         m=lis[i].text.strip()
         if re.match(r'^[\w\.\/]*',m):
            server=re.match(r'^[\w\.\/]*',m).group()
            print 'servert:'+server
            break;
         else:
            print 'server=NuLL'


    print '------------------------------------------------------------------------------------------------'


































































