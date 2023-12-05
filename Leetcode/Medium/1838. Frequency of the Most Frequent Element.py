"""
1838. Frequency of the Most Frequent Element
(Medium complexity)

The frequency of an element is the number of times it occurs in an array.

You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most k operations.
"""

class Solution:
    def maxFrequency(self, arr, k):
        ans = 1
        i = 0
        arr.sort()
        sum_ = 0

        for j in range(len(arr)):
            sum_ += arr[j]
            while sum_ + k < arr[j]*(j-i+1):
                sum_ -= arr[i]
                i +=1

            ans = max(ans, j - i + 1)
        return ans