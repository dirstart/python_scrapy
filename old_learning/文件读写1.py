# try:
#     f = open('D:/playing/python_file/test.txt', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()

with open('D:/playing/python_file/test.txt') as f:
	print(f.read())