"""
1701. Average Waiting Time
(Medium complexity)

There is a restaurant with a single chef. You are given an array customers, where customers[i] = [arrivali, timei]:

arrivali is the arrival time of the ith customer. The arrival times are sorted in non-decreasing order.
timei is the time needed to prepare the order of the ith customer.
When a customer arrives, he gives the chef his order, and the chef starts preparing it once he is idle. The customer waits till the chef finishes preparing his order. The chef does not prepare food for more than one customer at a time. The chef prepares food for customers in the order they were given in the input.

Return the average waiting time of all customers. Solutions within 10-5 from the actual answer are considered accepted.
"""


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)  # количество посетителей
        time = customers[0][1]  # время ожидания
        cur_wait = customers[0][0] + customers[0][1]  # текущее время начала ожидания для нового посетителя
        for come, prep in customers[1:]:  # проходим по посетителям
            time += max(0, cur_wait - come) + prep  # увеличиваем ожидание
            cur_wait = max(cur_wait + prep, come + prep)  # находим новое ожидание
        # ответ
        return time / n