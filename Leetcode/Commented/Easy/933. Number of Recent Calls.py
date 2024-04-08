"""
933. Number of Recent Calls
(Easy complexity)

You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.
"""


class RecentCounter:

    def __init__(self):
        self.queue = []  # очередь
        self.idx = 0  # указатель на последнее вхождение в диапазон [t - 3000, t]

    def ping(self, t: int) -> int:
        self.queue.append(t)  # добавляем в очередь
        while self.queue[self.idx] < t - 3000:  # пока вышли за диапазон - сдвигаем указатель
            self.idx += 1
        # ответ
        return len(self.queue) - self.idx


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)