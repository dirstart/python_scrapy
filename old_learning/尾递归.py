def solve(n):
	return fact(n,1)

def fact(num,product):
	if num==1:
		return product
	return fact(num-1,product*num)
print(solve(4))