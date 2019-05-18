import requests
import re
n = input('请输入你想查找的名字:')
url =requests.get('http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1538306701014_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word='+str(n))
url = url.text
pat = '"objURL":"(http://.*?)",'
s=0
content = re.findall(pat,url)
print('现在开始下载图片')
for addr in content:
    try:
        picture = requests.get(addr,timeout=10)
    except requests.exceptions.ConnectionError:
        print('这张有错跳过')
        continue
    s+=1
    s=str(s)
    f=open('D:/爬虫/百度爬取的图片/'+n+s+'.jpg','ab')
    s=int(s)
    f.write(picture.content)
    f.close()
