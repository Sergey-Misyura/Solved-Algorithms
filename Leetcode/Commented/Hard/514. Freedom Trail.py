"""
514. Freedom Trail
(Hard complexity)

In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial called the "Freedom Trail Ring" and use the dial to spell a specific keyword to open the door.

Given a string ring that represents the code engraved on the outer ring and another string key that represents the keyword that needs to be spelled, return the minimum number of steps to spell all the characters in the keyword.

Initially, the first character of the ring is aligned at the "12:00" direction. You should spell all the characters in key one by one by rotating ring clockwise or anticlockwise to make each character of the string key aligned at the "12:00" direction and then by pressing the center button.

At the stage of rotating the ring to spell the key character key[i]:

You can rotate the ring clockwise or anticlockwise by one place, which counts as one step. The final purpose of the rotation is to align one of ring's characters at the "12:00" direction, where this character must equal key[i].
If the character key[i] has been aligned at the "12:00" direction, press the center button to spell, which also counts as one step. After the pressing, you could begin to spell the next character in the key (next stage). Otherwise, you have finished all the spelling.
"""


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)  # длина кольца
        m = len(key)  # длина ключа

        places = defaultdict(list)  # словарь расположений букв
        for i, sym in enumerate(ring):
            places[sym].append(i)
        heap = [(0, 0, 0)]  # heap букв - затраты, индекс букв в ring, индекс буквы в key
        visited = set()  # посещенные буквы

        while heap:  # пока есть heap
            total, r_idx, k_idx = heapq.heappop(heap)  # получаем значение из heap
            if k_idx == m:  # если прошли весь ключ - останавливаем
                break
            if (r_idx, k_idx) not in visited:  # если r_idx, k_idx еще не проверяли
                visited.add((r_idx, k_idx))  # добавляем r_idx, k_idx в visited
                for nxt in places[key[k_idx]]:  # проходим по возможным вариантам нажатия key на ring
                    btw = abs(r_idx - nxt)  # расстояние по часовой
                    ard = n - btw  # расстояние против часовой
                    heapq.heappush(heap, (total + min(btw, ard), nxt, k_idx + 1))  # добавляем в heap варианты пути по часовой и против часовой стрелок
        # ответ total + длина ключа (на нажатия)
        return total + m
