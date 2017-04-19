import urllib
import urllib.request

def saveFile(data):
	save_path='D:\\temp.out'
	f_obj=open(save_path,'wb')  #wb表示打开方式
	f_obj.write(data)
	f_obj.close()

url="http://baidu.com"
data=urllib.request.urlopen(url).read()
data=data.decode('utf-8')
saveFile(data)

