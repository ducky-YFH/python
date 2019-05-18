import urllib.request,re
url=urllib.request.urlopen('http://news.sohu.com/').read()
urldecode=url.decode('utf-8','ignore')
guanjianci='href="(http://www.sohu.com/.*?)"'
allurl=re.compile(guanjianci).findall(urldecode)
for i in range(0,len(allurl)):
    print('现在爬到：'+str(i))
    file='D:/练习/'+'网页'+str(i)+'.html'
    urllib.request.urlretrieve(allurl[1],file)
