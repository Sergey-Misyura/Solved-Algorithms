"""
57. Insert Interval
(Medium complexity)

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.
"""


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        answer = []  # массив ответа
        i = 0  # индекс в массиве intervals
        while i < len(intervals) and intervals[i][1] < newInterval[0]:  # пока интервалы левее newInterval, добавляем в ответ
            answer.append(intervals[i])
            i += 1
        if i == len(intervals):  # если все интервалы были левее - добавляем newInterval в конец answer
            answer += [newInterval]
        else:  # в случае когда нашли интервал с концов на newInterval или за ним
            if intervals[i][0] <= newInterval[1]:  # если начало текущего интервала до или на newInterval
                answer.append([min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])])  # соединяем текущий интервал с newInterval, добавляем в answer
                i += 1
                while i < len(intervals) and intervals[i][0] <= answer[-1][1]:  # пока не вышли за границы intervals и последний интервал в answer пересекает текущий
                    answer[-1][1] = max(answer[-1][1], intervals[i][1])  # добавляем к последнему в answer текущий интервал
                    i += 1
                for j in range(i, len(intervals)):  # добавляем оставшиеся в intervals интервалы в answer
                    answer.append(intervals[j])
            else:  # если текущий интервал за newInterval
                answer.append(newInterval)  # добавляем в answer newInterval
                while i < len(intervals):  # добавляем в answer оставшиеся интервалы из intervals
                    answer.append(intervals[i])
                    i += 1
        # ответ
        return answer