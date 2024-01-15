"""
2225. Find Players With Zero or One Losses
(Medium complexity)

You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.
"""

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners, losers = zip(*matches)
        winners = set(winners) - set(losers)
        count_lose = Counter(losers)
        losers = [key for key, value in count_lose.items() if value == 1]

        return [sorted(list(winners)), sorted(losers)]