"""
752. Open the Lock
(Medium complexity)

You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.
"""


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def rotations(cur): # функция расчета номеров после прокрутки от cur
            rot_lst = []  # массив номеров
            for i in range(4):  # прокручиваем каждый номер
                first = int(cur[i])
                for shift in (-1, 1):  # движение цифры в номере
                    second = (first + shift + 10) % 10  # новая цифра в номере
                    rot_lst.append(cur[:i] + str(second) + cur[i + 1:])  # добавляем новый номер
            return rot_lst

        wrong = set(deadends)  # номера остановки и посещенные номера
        if '0000' in wrong:  # частный случай начального номера
            return -1
        queue = deque(['0000'])  #  текущая очередь номеров для прокрутки
        turns = 0  # количество прокруток
        while queue:  # пока есть номера в очереди
            for _ in range(len(queue)):  # проходим по текущим вариантам
                cur = queue.popleft()
                if cur == target:  # если пришли к target - возвращаем cur
                    return turns
                for next_val in rotations(cur):  # получаем следующие от cur номера при прокрутке rotations
                    if next_val not in wrong:  # если номер не в wrong - добавляем в очередь
                        wrong.add(next_val)
                        queue.append(next_val)
            turns += 1
        # возвращаем -1 если не дошли до target
        return -1

