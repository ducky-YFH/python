import urllib.request,re
keyname="睡衣"
key=urllib.request.quote(keyname)
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5193.400 QQBrowser/10.0.1066.400")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
for i in range(1,3):
    url="https://s.taobao.com/search?q="+key+"&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180621&ie=utf8&bcoffset=0&ntoffset=6&p4ppushleft=1%2C48&s="+str(i*44)
    data=urllib.request.urlopen(url).read().decode('utf-8','ignore')
    yaodian='pic_url":"//(.*?)"'
    allpic=re.compile(yaodian).findall(data)
    for j in range(0,len(allpic)):
        thisimg=allpic[j]
        nowpic="http://"+thisimg
        file="D:/练习/qq/"+str(i)+str(j)+'.jpg'
        urllib.request.urlretrieve(nowpic,file)
