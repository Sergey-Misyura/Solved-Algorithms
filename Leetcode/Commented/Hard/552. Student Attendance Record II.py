"""
552. Student Attendance Record II
(Hard complexity)

An attendance record for a student can be represented as a string where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

'A': Absent.
'L': Late.
'P': Present.
Any student is eligible for an attendance award if they meet both of the following criteria:

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Given an integer n, return the number of possible attendance records of length n that make a student eligible for an attendance award. The answer may be very large, so return it modulo 109 + 7.
"""


class Solution:
    def checkRecord(self, n: int) -> int:
        dp, mod = [1, 1, 0, 1, 0, 0], 10**9 + 7  # динамика, мод
        # динамика выглядит как количество вариантов при условиях: [(при A=0, L=0); (при A=0, L=1); (при A=0, L=2)
        # (при A=1, L=0); (при A=1, L=1); (при A=1, L=2)]
        for i in range(n - 1):
            cnt_noA, cnt_1A = sum(dp[:3]) % mod, sum(dp[3:]) % mod  # суммы при A=0, A=1
            dp = [cnt_noA, dp[0], dp[1], cnt_noA + cnt_1A, dp[3], dp[4]]  # пересчет динамики по условию
        # ответ
        return (sum(dp) % mod)

