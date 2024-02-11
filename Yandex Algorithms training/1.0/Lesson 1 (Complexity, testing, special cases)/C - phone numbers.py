s = input().strip()

s = s.replace("+", "").replace("-", "").replace("(", "").replace(")", "")
if len(s) == 7:
	s = '7495' + s

if s[0] != '7' and s[0] != '8':
    for _ in range(3):
        a = input().strip()
        print('NO')
else:
	for _ in range(3):
		old_s = input().strip()
		old_s = old_s.replace("+", "").replace("-", "").replace("(", "").replace(")", "")
		if len(old_s) == 7:
		    old_s = '7495' + old_s
		ans = 'YES' if s[1:] == old_s[1:] else 'NO'
		print(ans)