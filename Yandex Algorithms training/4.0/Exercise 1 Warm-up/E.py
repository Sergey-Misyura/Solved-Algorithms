n = int(input())
arr = list(map(int, input().split()))

ans = [0] * n  # answer - массив ответа (недовольств)
cur_diff = arr[0]  # current difference - текущее изменение рейтинга между текущим и предыдущим
# студентом
cur_disc = sum(arr) - cur_diff * n  # current discontent - текущее недовольство студентов
ans[0] = cur_disc

for i in range(1, n):
    # считаем current diffirence
    cur_diff = arr[i] - arr[i - 1]
    # уменьшаем предыдущее недовольство на изменение недовольства справа от i (cur_diff * (n - i))
    # и увеличеваем на изменение недовольства слева от i (cur_diff * i)
    # можно общий множитель вынести)
    cur_disc = cur_disc - cur_diff * (n - i) + cur_diff * i
    # запись в массив ответа
    ans[i] = cur_disc

print(*ans)
