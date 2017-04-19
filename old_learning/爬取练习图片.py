import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist      
   
html = getHtml("http://tieba.baidu.com/p/2460150866")
print getImg(html)
	# pic_ext 是匹配源里要包含的东西，也就是说源内容一定要以pic_ext结尾才匹配成功
