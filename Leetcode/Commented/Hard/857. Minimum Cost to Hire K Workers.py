"""
857. Minimum Cost to Hire K Workers
(Hard complexity)

There are n workers. You are given two integer arrays quality and wage where quality[i] is the quality of the ith worker and wage[i] is the minimum wage expectation for the ith worker.

We want to hire exactly k workers to form a paid group. To hire a group of k workers, we must pay them according to the following rules:

Every worker in the paid group must be paid at least their minimum wage expectation.
In the group, each worker's pay must be directly proportional to their quality. This means if a worker’s quality is double that of another worker in the group, then they must be paid twice as much as the other worker.
Given the integer k, return the least amount of money needed to form a paid group satisfying the above conditions. Answers within 10-5 of the actual answer will be accepted.
"""


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)  # количество работников
        total = float("inf")  # оплата для итоговой группы
        cur_total = 0  # текущее общее quality
        ratio = sorted([(w / q, q) for w, q in zip(wage, quality)])  # сортируем работников по wage/quality
        heap = []  # heap
        for i in range(n):  # проходим по работникам
            heappush(heap, - ratio[i][1])  # добавляем в heap
            cur_total += ratio[i][1]  # увеличиваем текущее общее quality
            if len(heap) > k:  # если в heap больше нужных k работников
                cur_total += heappop(heap)  # достаем из heap, увеличиваем текущее общее quality
            if len(heap) == k:  # когда нашли k работников - обновляем total
                total = min(total, cur_total * ratio[i][0])  # cur_total * больший коэффициент
        # ответ
        return total


