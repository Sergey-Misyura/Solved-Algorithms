"""
1700. Number of Students Unable to Eat Lunch
(Easy complexity)

The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:

If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
Otherwise, they will leave it and go to the queue's end.
This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the ith sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the jth student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.
"""


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stud_count = Counter(students)  # счетчик желаний студентов
        n, cur_sand = len(students), 0  # длина students, текущий индекс в sandwiches
        while cur_sand < n and stud_count[sandwiches[cur_sand]]:  # пока не вышли за пределы массива и есть студенты желающие сендвич
            stud_count[sandwiches[cur_sand]] -= 1  # уменьшаем счетчик
            cur_sand += 1  # двигаем указатель
        # ответ - длина остатка массива
        return n - cur_sand

