"""
621. Task Scheduler
(Medium complexity)

You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.

​Return the minimum number of intervals required to complete all tasks.
"""


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)  # счетчик количеств задач
        max_freq = max(freq.values())  # самая большая частота задачи
        freq = list(freq.values())  # список частот задач
        max_freq_count = 0  # количество задач с макс частотой
        i = 0  # индекс в freq
        while i < len(freq):  # проходим по частотам
            if freq[i] == max_freq:  # если частота соответствует максимальной - увеличиваем max_freq_count
                max_freq_count += 1
            i += 1
        # предполагаемое время - число периодов на длину периода + max_freq_count
        est_time = (max_freq - 1) * (n + 1) + max_freq_count
        # ответ - большее из числа задач или посчитанным времени
        return max(answer, len(est_time))