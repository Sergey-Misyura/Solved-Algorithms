"""
2540. Minimum Common Value
(Easy complexity)

Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.
"""


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        idx1, idx2 = 0, 0  # указатели чисел в массиве 1 и массиве 2
        # пока не вышли за пределы массивов и числа не равны
        while idx1 < len(nums1) and idx2 < len(nums2) and nums1[idx1] != nums2[idx2]:
            if nums1[idx1] > nums2[idx2]:  # если первое число больше - двигаем второй указатель
                idx2 += 1
            else:  # иначе двигаем первый указатель
                idx1 += 1
        # ответ
        # если вышли за пределы массива - -1
        if idx1 == len(nums1) or idx2 == len(nums2):
            return -1
        else:  # иначе искомое число
            return nums1[idx1]