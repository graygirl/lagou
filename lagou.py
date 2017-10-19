# -*- coding:utf-8 -*-
import urllib
import urllib.request
import re
import xlwt

from urllib import request
with request.urlopen("https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=%E7%8E%8B%E5%86%AC%202017/9/26%2018:27:45") as f:
    data = f.read()
    print('Status: ',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s: %s' %(k,v))
    print('Data: ',data.decode('utf-8'))



