a = int(input().strip())
b = int(input().strip())
c = int(input().strip())

if a + b > c and a + c > b and b + c > a:
	print('YES')
else:
	print('NO')