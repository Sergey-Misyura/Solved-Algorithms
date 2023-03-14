letters_list = []
N = int(input())
for _ in range(N):
    letters_list.append(int(input()))
   
good_number = 0

for i in range(len(letters_list)-1):
    good_number += min(letters_list[i], letters_list[i+1])
   
print(good_number)