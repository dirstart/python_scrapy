import urllib
import urllib.request

url="http://baidu.com"
data=urllib.request.urlopen(url).read()
data=data.decode('utf-8')

with open('D:/playing/python_file/baidu.txt','w') as f:
	f.write(data)