import urllib
import urllib.request

url="http://www.fgm.cc/learn/"
data=urllib.request.urlopen(url).read()
data=data.decode('utf-8')

with open('D:/playing/python_file/fgm.html','wb') as f:
	f.write(data)