"""
2751. Robot Collisions
(Hard complexity)

There are n 1-indexed robots, each having a position on a line, health, and movement direction.

You are given 0-indexed integer arrays positions, healths, and a string directions (directions[i] is either 'L' for left or 'R' for right). All integers in positions are unique.

All robots start moving on the line simultaneously at the same speed in their given directions. If two robots ever share the same position while moving, they will collide.

If two robots collide, the robot with lower health is removed from the line, and the health of the other robot decreases by one. The surviving robot continues in the same direction it was going. If both robots have the same health, they are both removed from the line.

Your task is to determine the health of the robots that survive the collisions, in the same order that the robots were given, i.e. final heath of robot 1 (if survived), final health of robot 2 (if survived), and so on. If there are no survivors, return an empty array.

Return an array containing the health of the remaining robots (in the order they were given in the input), after no further collisions can occur.

Note: The positions may be unsorted.
 """


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        stack = []  # стек роботов
        for i, pos in sorted(enumerate(positions), key=lambda x: x[1]):  # проходим по сортированным роботам
            cur_dir, cur_hp = directions[i], healths[i]
            if cur_dir == 'R':  # если робот движется вправо, добавляем в стек
                stack.append((i, cur_hp, cur_dir, pos))
            else:  # если робот движется влево
                while stack and stack[-1][2] == 'R' and cur_dir == 'L' and cur_hp != 0: # и сталкивается с предыдущим
                    prev_i, prev_hp, prev_dir, prev_pos = stack.pop()  # достаем предыдущего робота из стека
                    if prev_hp > cur_hp:  # если предыдущий робот "выйграл" меняем его с текущим
                        i, cur_dir, pos = prev_i, prev_dir, prev_pos
                    cur_hp = 0 if cur_hp == prev_hp else max(cur_hp, prev_hp) - 1  # обновляем cur_hp после столкновения
                if cur_hp != 0:  # если один остался, добавляем в стек
                    stack.append((i, cur_hp, cur_dir, pos))
        res = dict()  # словарь итоговых позиций
        for _, cur_hp, _, cur_pos in stack:  # добавляем роботов в словарь
            res[cur_pos] = cur_hp
        # проходим по исходным позициям и составляем ответ из hp оставшихся роботов
        return [res[pos] for pos in positions if pos in res]