"""
1431. Kids With the Greatest Number of Candies
(Easy complexity)

There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.
"""


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)  # наибольшее число конфет в candies
        answer = [False] * len(candies)  # массив ответа
        for i in range(len(candies)):  # проходим по candies
            if candies[i] + extraCandies >= max_candy:  # если при добавлении получили не меньше max_candy, обновляем answer[i] на True
                answer[i] = True
        # ответ
        return answer