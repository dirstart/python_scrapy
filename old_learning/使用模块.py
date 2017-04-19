#
#
'a test module'
__author__="chenhongpeng"
import sys

def test():
	args=sys.argv
	if len(args)==1:
		print("hello,world")
	elif len(args)==2:
		print("hello,chenhongpeng")
	else:
		print("hello,<li></li>")

test()
print(__name__=='__main__')