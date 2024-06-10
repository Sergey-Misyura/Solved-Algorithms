"""
846. Hand of Straights
(Medium complexity)

Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.
"""


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)  # счетчик карт
        for key in sorted(count):  # прохлдим по сортированным значениям карт
            if count[key] > 0:  # пока есть карты для key
                cur = count[key]  # текущее количество для key
                for i in range(groupSize):  # формируем группу
                    count[key + i] -= cur  # последующие значение уменьшаем на число cur
                    if count[key + i] < 0:  # если карт недостаточно - ответ False
                        return False
        return True