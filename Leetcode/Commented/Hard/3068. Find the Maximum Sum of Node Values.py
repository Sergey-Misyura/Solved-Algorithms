"""
3068. Find the Maximum Sum of Node Values
(Hard complexity)

There exists an undirected tree with n nodes numbered 0 to n - 1. You are given a 0-indexed 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the tree. You are also given a positive integer k, and a 0-indexed array of non-negative integers nums of length n, where nums[i] represents the value of the node numbered i.

Alice wants the sum of values of tree nodes to be maximum, for which Alice can perform the following operation any number of times (including zero) on the tree:

Choose any edge [u, v] connecting the nodes u and v, and update their values as follows:
nums[u] = nums[u] XOR k
nums[v] = nums[v] XOR k
Return the maximum possible sum of the values Alice can achieve by performing the operation any number of times.
 """


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        max_sum, change_count, min_abs_change = 0, 0, float('inf')  # максимальная сумма, количество изменений, мин изменение
        for n in nums:  # проходим по nums
            xor = n ^ k  # xor
            max_sum += max(n, xor)  # увеличиваем max_sum на лучшее из n и max_xor
            min_abs_change = min(abs(n - xor), min_abs_change)  # обновляем мин изменение
            if xor > n:  # если выбрали xor - увеличиваем change_count
                change_count += 1
        if not change_count % 2:  # если четное количество операций - возвращаем ответ
            return max_sum
        # если нечетное - откатывается на min_abs_change
        return max_sum - min_abs_change
