"""
1630. Arithmetic Subarrays
(Medium complexity)

A sequence of numbers is called arithmetic if it consists of at least two elements, and the difference between every two consecutive elements is the same. More formally, a sequence s is arithmetic if and only if s[i+1] - s[i] == s[1] - s[0] for all valid i.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic:

1, 1, 2, 5, 7
You are given an array of n integers, nums, and two arrays of m integers each, l and r, representing the m range queries, where the ith query is the range [l[i], r[i]]. All the arrays are 0-indexed.

Return a list of boolean elements answer, where answer[i] is true if the subarray nums[l[i]], nums[l[i]+1], ... , nums[r[i]] can be rearranged to form an arithmetic sequence, and false otherwise.

"""


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(arr):
            min_num, max_num = min(arr), max(arr)
            if (max_num - min_num) % (len(arr) - 1):
                return False
            diff = (max_num - min_num) // (len(arr) - 1)
            if diff == 0:
                return True
            diffs_arr = [0] * len(arr)
            for num in arr:
                if (num - min_num) % diff:
                    return False
                diffs_arr[(num - min_num) // diff] = 1
            return False if 0 in diffs_arr else True

        ans = []
        for start, end in zip(l, r):
            ans.append(check(nums[start:end + 1]))

        return ans