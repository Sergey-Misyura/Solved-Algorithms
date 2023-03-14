N, M, K = tuple(map(int, input().split()))

matrix = []

#первая строка матрицы
s = list(map(int, input().split()))
pref, pref_list = 0, []
for k in range(len(s)):
    pref_list.append(s[k]+pref)
    pref+=s[k]
matrix.append(pref_list)

# дозаполнение матрицы
for i in range(1,N):
    s = list(map(int, input().split()))
    matrix.append([])
    matrix[i].append(matrix[i-1][0]+s[0])
    for j in range(1,len(s)):
        matrix[i].append(matrix[i-1][j]+matrix[i][j-1]-matrix[i-1][j-1]+s[j])
# запросы
for _ in range(K):
    x1, y1, x2, y2 = tuple(map(lambda x: x - 1, tuple(map(int, input().split()))))
    if x1==0 and y1==0:
        print(matrix[x2][y2])
    elif x1==0:
        print(matrix[x2][y2] - matrix[x2][y1-1])
    elif y1==0:
        print(matrix[x2][y2] - matrix[x1-1][y2])
    else:
        print(matrix[x2][y2]-matrix[x2][y1-1]-matrix[x1-1][y2]+matrix[x1-1][y1-1])