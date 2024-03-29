# считываем данные
n = int(input())  # границы загадываемого числа
nums_yes = set(map(str, range(1, n + 1)))  # множество чисел, с загаданным числом
question = input()  # задаваемый вопрос
answer = []  # массив ответа
# пока вопрос не HELP
while question != 'HELP':
    question = set(question.split())  # множество чисел вопроса
    # если при ответе YES множество ответов уменьшится более чем в 2 раза
    if len(nums_yes & question) <= len(nums_yes) / 2:
        # отвечаем NO, уменьшаем множество nums_yes
        answer.append('NO')
        nums_yes -= question
    # иначе отвечаем YES, в множестве оставляем пересечение множеств
    else:
        answer.append('YES')
        nums_yes = nums_yes & question
    question = input().strip()

# ответ
print(*answer, sep='\n')
# выводим список чисел
print(*sorted(list(map(int, nums_yes))))