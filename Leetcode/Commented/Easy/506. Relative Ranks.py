"""
506. Relative Ranks
(Easy complexity)

You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.
"""


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)  # длина массива очков
        sort_score = sorted([(scr, i) for i, scr in enumerate(score)], reverse=True)  # отсортированный массив очков с индексами
        score[sort_score[0][1]] = "Gold Medal"  # ставим на 1 место золотую медаль
        if n > 1:
            score[sort_score[1][1]] = "Silver Medal"  # ставим на 2 место серебрянную медаль
        if n > 2:
            score[sort_score[2][1]] = "Bronze Medal"  # ставим на 3 место бронзовую медаль
        for i in range(3, n):  # заменяем оставшиеся места числами
            score[sort_score[i][1]] = str(i + 1)
        # ответ
        return score