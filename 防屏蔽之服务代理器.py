import urllib.request
def use_proxy(url,proxy_addr): #proxy:代理服务器 
    proxy=urllib.request.ProxyHandler({"http":proxy_addr}) #Handler：处理者
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data=urllib.request.urlopen(url).read().decode('utf-8','ignore')
    return data
proxy_addr="119.183.220.224:8888"
url='http://www.baidu.com'
data=use_proxy(url,proxy_addr)
print(len(data))
