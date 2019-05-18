import requests
import re
import json
import time

url = 'http://lol.qq.com/biz/hero/champion.js'
response = requests.get(url).content
new = response.decode()

pat='"keys":(.*?),"data"' #找到英雄字典
data = re.findall(pat,new)
heroID = []
heroName = []
for i in heroName:
    print(i)
for dict in data:
    dict = eval(dict)
    for id in dict:
        heroID.append(id)
        heroName.append(dict[id])
#print(heroID)

#定义图片列表
pic_list = []
for k in heroID:
    for i in range(20):
        num = str(i)
        if len(num) == 1:
            hero_num = '00'+ num
        elif len(num) == 2:
            hero_num = '0' + num
        picurl='http://ossweb-img.qq.com/images/lol/web201310/skin/big'+str(k)+hero_num+'.jpg'
        pic_list.append(picurl)
#获取图片名称
list_filepath=[]
path = 'D:\下载\爬虫\英雄联盟\\'
for name in heroName:
    for i in range(20):
        file_path=path+name+str(i)+'.jpg'
        list_filepath.append(file_path)

'''
n=0
for picurl in pic_list:
    res = requests.get(picurl)
    n += 1
    if res.status_code == 200:
        print('正在下载%s'%list_filepath[n])
        time.sleep(1)
        with open(list_filepath[n],'wb') as f:
            f.write(res.content)
'''

