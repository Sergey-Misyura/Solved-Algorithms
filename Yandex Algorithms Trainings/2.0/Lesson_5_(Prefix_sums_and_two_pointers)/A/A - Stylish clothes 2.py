from heapq import heappop, heappush, heapify

# считываем данные
count_1 = int(input().strip())  # количество вещей из массива 1
arr_1 = list(map(int, input().split()))  # массив вещей 1
count_2 = int(input().strip())  # количество вещей из массива 2
arr_2 = list(map(int, input().split()))  # массив вещей 2
count_3 = int(input().strip())  # количество вещей из массива 3
arr_3 = list(map(int, input().split()))  # массив вещей 3
count_4 = int(input().strip())  # количество вещей из массива 4
arr_4 = list(map(int, input().split()))  # массив вещей 4
# сортируем массивы
arr_1.sort()
arr_2.sort()
arr_3.sort()
arr_4.sort()

# создаем heap текущих цветов в каждом массиве типа: (цвет, массив, индекс в массиве)
heap = [(arr_1[0], 1, 0), (arr_2[0], 2, 0), (arr_3[0], 3, 0), (arr_4[0], 4, 0)]

heapify(heap)  # преобразование массива в heap
answer = heap.copy()  # переменная ответа
heap_max = max(arr_1[0], arr_2[0], arr_3[0], arr_4[0])  # максимальный элемент в heap
answer_diff = heap_max - heap[0][0]  # разница текущих max и min цветов
_, cur_arr, cur_idx = heappop(heap)  # достаем младший элемент из heap, его индекс и массив
cur_idx += 1  # переходим к следующему элементу
# продолжаем пока не вышли за пределы одного из массивов
while (cur_arr == 1 and cur_idx < count_1) or (cur_arr == 2 and cur_idx < count_2) \
    or (cur_arr == 3 and cur_idx < count_3) or (cur_arr == 4 and cur_idx < count_4):
    cur_push = (0, 0, 0)  # новый запушиваемый в heap элемент
    # обновляем cur_push в соответствии с массивом cur_arr
    if cur_arr == 1:
        cur_push = (arr_1[cur_idx], 1, cur_idx)
    elif cur_arr == 2:
        cur_push = (arr_2[cur_idx], 2, cur_idx)
    elif cur_arr == 3:
        cur_push = (arr_3[cur_idx], 3, cur_idx)
    elif cur_arr == 4:
        cur_push = (arr_4[cur_idx], 4, cur_idx)
    heappush(heap, cur_push)  # пушим новый элемент в heap
    heap_max = max(heap_max, cur_push[0])  # обновляем heap_max
    if answer_diff > heap_max - heap[0][0]:  # если разница цветов стала меньше - обновляем answer_diff и answer
        answer_diff = heap_max - heap[0][0]
        answer = heap.copy()
    _, cur_arr, cur_idx = heappop(heap)  # достаем младший элемент из heap
    cur_idx += 1  # переходим к следующему элементу

answer_arr = [0] * 4  # массив вывода
for color, arr, _ in answer:
    answer_arr[arr - 1] = color
# ответ
print(*answer_arr)