# считываем данные
_ = input()
nums1 = set(map(int, input().split()))  # массив чисел 1
_ = input()
nums2 = set(map(int, input().split()))  # массив чисел 2
_ = input()
nums3 = set(map(int, input().split()))  # массив чисел 3

inter1 = nums1.intersection(nums2)  # пересекаем массивы 1 и 2
inter2 = nums1.intersection(nums3)  # пересекаем массивы 1 и 3
inter3 = nums2.intersection(nums3)  # пересекаем массивы 2 и 3

answer = inter1 | inter2 | inter3  # объединяем массивы
# ответ
print(*sorted(answer))