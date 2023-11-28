from collections import defaultdict

word1 = input()
word2 = input()

dic1 = defaultdict(int)
dic2 = defaultdict(int)

for sym in word1:
    dic1[sym] +=1
for sym in word2:
    dic2[sym] +=1

if dic1==dic2:
    print('YES')
else:
    print('NO')