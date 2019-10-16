# coding=utf-8  
import re  
import urllib

url = "http://www.baidu.com/"  
content = urllib.urlopen(url).read()

#获取完整超链接
res = r"<a.*?href=.*?<\/a>"
urls = re.findall(res, content)
for u in urls:
    print unicode(u,'utf-8')

#获取超链接<a>和</a>之间内容
res = r'<a .*?>(.*?)</a>'  
texts = re.findall(res, content, re.S|re.M)  
for t in texts:
    print unicode(t,'utf-8')
