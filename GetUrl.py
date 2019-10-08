def GetUrl(url):
    urls=url.split('/')
    url=urls[0]+'//'+urls[1]+'/'+urls[2]+'/'+urls[3]+'/'
    return url

testurl=GetUrl("https://coding.imooc.com/class/")+"chapter/269.html#Anchor"
print(testurl)
