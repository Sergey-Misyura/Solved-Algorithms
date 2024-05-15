"""
787. Cheapest Flights Within K Stops
(Medium complexity)

There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.
"""


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(dict)  # граф
        for s, d, w in flights:  # добавляем полеты в граф
            graph[s][d] = w
        heap = [(0, src, k+1)]  # heap
        vis = [0] * n  # число состановок для каждого города
        while heap:  # пока есть heap
            w, x, k = heapq.heappop(heap)  # достаем из heap рейс с цена, отправление, перелеты
            if x == dst:  # если нашли место назначения - возвращаем w
                return w
            if vis[x] >= k:  # если число остановок >= k переходим к следующему
                continue
            vis[x] = k  # устанавливаем текущее число остановок для x как k
            for y, dw in graph[x].items():  # проходим по связанным с x городам
                heapq.heappush(heap, (w+dw, y, k-1))  # добавляем соседей с увеличением цены и k-1 остановками
        # если не нашли путь - ответ -1
        return -1
