# -*- coding: utf-8 -*-
import requests
import time
import datetime

url = "http://www.hshfy.sh.cn/shfy/gweb/ktgg_search_content.jsp?"

page_num = 1
date_time = datetime.date.fromtimestamp(time.time())
print date_time

data = {
    "pktrqks": date_time,
    "ktrqjs": date_time,
    "pagesnum": page_num
}
print data

content = requests.get(url, data, timeout=3)
content.encoding='gbk'
print content.text
