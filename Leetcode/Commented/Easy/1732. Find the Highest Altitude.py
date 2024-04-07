"""
1732. Find the Highest Altitude
(Easy complexity)

There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
"""

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        pref_sum = [0] * (len(gain) + 1)  # массив преф сумм
        for i in range(len(gain)):
            pref_sum[i + 1] = pref_sum[i] + gain[i]
        # ответ - максимум в массиве
        return max(pref_sum)