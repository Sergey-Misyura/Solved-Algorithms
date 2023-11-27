from math import ceil

a = int(input())
b = int(input())
n = int(input())

min_stu_1 = a
min_stu_2 = ceil(b/n)

if min_stu_1 > min_stu_2:
    print('Yes')
else:
    print('No')