"""
31. Next Permutation
(Medium complexity)

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory."""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        first_desc = n - 1
        while first_desc > 0 and nums[first_desc - 1] >= nums[first_desc]:
            first_desc -= 1
        if first_desc == 0:
            nums.reverse()
            return

        repl = first_desc - 1
        from_repl = n - 1
        while nums[from_repl] <= nums[repl]:
            from_repl -= 1
        nums[from_repl], nums[repl] = nums[repl], nums[from_repl]

        lf, rg = repl + 1, n - 1
        while lf < rg:
            nums[lf], nums[rg] = nums[rg], nums[lf]
            lf += 1
            rg -= 1

