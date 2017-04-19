import re
text="what fuck"
m=re.match(r"(\w+)\s",text)
print(m)

# \w表示字母或者数字， \s表示空格