import urllib
import urllib.request
import os
L=[]
K=[]
nl=1
nk=1
while nl<=10:
	L.append("lesson"+str(nl))
	nl=nl+1
while nk<=9:
	K.append("0"+str(nk))
	nk=nk+1
	
	# 我们要先在磁盘上创建这些目录才存放我们要爬取的网页，这是我真正意义上的第一个爬虫
	my_path='D:/playing/python_file2'
	for x in L:
		try:
			os.mkdir(os.path.join(my_path,x))
		except Exception as e:
			continue
		# 按教程说推荐使用join来拼接字符而不是直接相加


	for x in L:	
		for y in K:
			url='http://www.fgm.cc/learn/'
			full_url=url+x+'/'+y+".html"
			print(full_url)
			req=urllib.request.Request(full_url,headers={
				'Connection':'Keep-Alive',
				'Accept':'text/html, application/xhtml+xml, */*',
				'Accept-Language':'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
				'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
				})			
			try:
				oper = urllib.request.urlopen(req)
				data=oper.read()
				with open(my_path+'/'+x+'/'+y+'.html','wb') as f:
					f.write(data)
			except:
				continue


		