# считываем данные
n = int(input().strip())  # количество сообщений

themes = []  # массив тем сообщений, i - номер темы, [k, theme_name] - количество сообщений, название темы
added_theme_n = 0  # номер следующей добавляемой темы
messages = [-1]*(n+1)  # массив тем сообщений: i - номер cообщения, [i] - номер темы в сообщении
max_messages = 1  # максимальное число сообщений для всех тем
# проходим по сообщениям
for i in range(1, n + 1):
    address = int(input().strip())  # описание сообщения
    # если создана новая тема,
    if address == 0:
        theme = input().strip()
        themes.append([1, theme])  # добавляем 1 сообщение и тему к themes
        message = input().strip()
        messages[i] = added_theme_n  # в messages[i] сохраняем тему сообщения
        added_theme_n += 1  # увеличиваем номер темы
    # если сообщение является ответом
    else:
        message = input().strip()
        cur_theme_n = messages[address]  # получаем номер темы из адресуемого сообщения
        themes[cur_theme_n][0] += 1  # увеличиваем число сообщений темы
        messages[i] = cur_theme_n  # в messages[i] сохраняем тему сообщения
        max_messages = max(max_messages, themes[cur_theme_n][0])  # обновляем max_messages

# проходим по темам и выводим в ответ первую с max_messages
for count_messages, theme in themes:
    if count_messages == max_messages:
        print(theme)
        break
