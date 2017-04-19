import urllib
import urllib.request
 
values = {}
values['username'] = "1016903103@qq.com"
values['password'] = "XXXX"
data = values.urlencode() 
url = "http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib.request.Request(url,data)
response = urllib.request.urlopen(request)
print (response.read())