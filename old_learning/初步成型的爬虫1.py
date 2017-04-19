import urllib
import urllib.request
request=urllib.request.Request("http://www.baidu.com")
response=urllib.request.urlopen(request)
data=response.read()
data=data.decode('utf-8')
print(data)