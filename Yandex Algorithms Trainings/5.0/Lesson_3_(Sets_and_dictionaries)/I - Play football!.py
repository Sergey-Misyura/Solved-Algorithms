# считываем данные через файл
with open('input.txt', 'r') as f:
    answer = []  # массив ответа
    teams = dict()   # словарь команд вида - team:[total_goals, matches, score_opens]   # score_opens - количество первых голов в матче командой
    players = dict()  # словарь игроков вида - player:[total_goals, team, score_opens, [0]*91]  # score_opens - количество первых голов в матче игроком, [0]*91 - массив всех голов игрока на минуте i
    line = f.readline().strip()  # читаем первую строку файла

    while line != '':  # продолжаем пока файл не закончится
        if line.startswith('Total goals for'):  # запрос на Общее число голов команды
            team = line[15:].replace('"', '').strip()  # получаем название команды
            if team in teams.keys():  # если есть команда в teams, сохраняем в answer общее число голов
                answer.append(teams[team][0])
            else:  # иначе сохраняем в answer 0
                answer.append(0)
        elif line.startswith('Mean goals per game for'):  # запрос на Среднее число голов команды в матче
            team = line[23:].replace('"', '').strip()  # получаем название команды
            if team in teams.keys():  # если есть команда в teams, сохраняем в answer все голы / матчи команды
                answer.append(teams[team][0] / teams[team][1])
            else:  # иначе сохраняем в answer 0
                answer.append(0)
        elif line.startswith('Total goals by'):  # запрос на Общее число голов игрока
            player = line[14:].strip()  # получаем фамилию/прозвище игрока
            if player in players.keys():  # если игрок есть в players, сохраняем в answer общее число голов
                answer.append(players[player][0])
            else:  # иначе сохраняем в answer 0
                answer.append(0)
        elif line.startswith('Mean goals per game by'):  # запрос на Среднее число голов игрока в матче
            player = line[22:].strip()  # получаем фамилию/прозвище игрока
            if player in players.keys():  # если игрок есть в players
                team = players[player][1]  # получаем название команды игрока
                answer.append(players[player][0] / teams[team][1])  # сохраняем в answer голы игрока / число матчей команды
            else:  # иначе сохраняем в answer 0
                answer.append(0)
        elif line.startswith('Goals on minute'):  # запрос на Число голов игрока во всех матчах на заданной минуте
            minute, player = line[15:].split(' by ')  # получаем минуту и фамилию/прозвище игрока
            minute = int(minute.strip())
            player = player.strip()
            if player in players.keys():  # если игрок есть в players - сохраняем в answer голы на заданной минуте
                answer.append(players[player][3][minute])
            else:  # иначе сохраняем в answer 0
                answer.append(0)
        elif line.startswith('Goals on first'):  # запрос на Число голов игрока во всех матчах за первые x заданных минут
            minute, player = line[14:].split('minutes by')  # получаем минуту и фамилию/прозвище игрока
            minute = int(minute.strip())
            player = player.strip()
            if player in players.keys():  # если игрок есть в players - сохраняем в answer сумму голов по заданную минуту
                answer.append(sum(players[player][3][:minute + 1]))
            else:  # иначе сохраняем в answer 0
                answer.append(0)
        elif line.startswith('Goals on last'):  # запрос на Число голов игрока во всех матчах за последние x заданных минут
            minute, player = line[13:].split('minutes by')  # получаем минуту и фамилию/прозвище игрока
            minute = int(minute.strip())
            player = player.strip()
            if player in players.keys():  # если игрок есть в players - сохраняем в answer сумму голов за последние x заданных минут
                answer.append(sum(players[player][3][91 - minute:]))
            else:  # иначе сохраняем в answer 0
                answer.append(0)
        elif line.startswith('Score opens by'):  # запрос на Количество открытий счета в матче
            if line[15] == '"':  # если в запросе команда
                team = line[14:].replace('"', '').strip()  # получаем название команды
                if team in teams.keys():  # если команда есть в teams - сохраняем в answer количество открытий счета командой
                    answer.append(teams[team][2])
                else:  # иначе сохраняем в answer 0
                    answer.append(0)
            else:  # если в запросе игрок
                player = line[14:].strip()  # получаем фамилию/прозвище игрока
                if player in players.keys():  # если игрок есть в players - сохраняем в answer количество открытий счета игроком
                    answer.append(players[player][2])
                else:  # иначе сохраняем в answer 0
                    answer.append(0)
        else:  # если в строке содержится информация о матче
            team1, team2_score = line.split('-')  # получаем название первой команды и оставшуюся часть строки
            team1 = team1.replace('"', '').strip()
            team2, score = team2_score.split('" ')  # получаем название второй команды и оставшуюся часть строки
            team2 = team2.replace('"', '').strip()
            score1, score2 = map(int, score.split(':'))  # получаем счет матча

            if team1 not in teams.keys():  # если команды 1 нет в teams - добавляем ее с score1 и первым матчем
                teams[team1] = [score1, 1, 0]
            else:  # иначе увеличиваем счетчик голов и счетчик матчей team1
                teams[team1][0] += score1
                teams[team1][1] += 1
            if team2 not in teams.keys():  # если команды 2 нет в teams - добавляем ее с score2 и первым матчем
                teams[team2] = [score2, 1, 0]
            else:  # иначе увеличиваем счетчик голов и счетчик матчей team2
                teams[team2][0] += score2
                teams[team2][1] += 1
            # сообщения голов в матче для team1
            first_goal_team1, time_first_goal_team1 = '', 99  # игрок забивший первый гол у team1, время первого гола у team1
            for i in range(score1):  # проходим по сообщениям голов первой команды в матче
                line = f.readline().strip().split()  # сообщение о голе
                scored_player, goal_time = ' '.join(line[:-1]), int(line[-1][:-1])  # получаем фамилию/прозвище забившего игрока, время гола
                if scored_player not in players.keys():  # если игрока нет в players
                    players[scored_player] = [1, team1, 0, [0] * 91]  # добавляем игрока в players с первым голом и его командой
                else:  # если игрок есть в players
                    players[scored_player][0] += 1  # увеличиваем счетчик его голов
                players[scored_player][3][goal_time] += 1  # увеличиваем счетчик голов игрока на минуте goal_time
                if i == 0:  # если текущий гол - первый гол команды в матче, обновляем first_goal_team1 и time_first_goal_team1
                    first_goal_team1, time_first_goal_team1 = scored_player, goal_time
            # сообщения голов в матче для team2
            first_goal_team2, time_first_goal_team2 = '', 99  # игрок забивший первый гол у team2, время первого гола у team2
            for i in range(score2):  # проходим по сообщениям голов второй команды в матче
                line = f.readline().strip().split()  # сообщение о голе
                scored_player, goal_time = ' '.join(line[:-1]), int(line[-1][:-1])  # получаем фамилию/прозвище забившего игрока, время гола
                if scored_player not in players.keys():  # если игрока нет в players
                    players[scored_player] = [1, team2, 0, [0] * 91]  # добавляем игрока в players с первым голом и его командой
                else:  # если игрок есть в players
                    players[scored_player][0] += 1  # увеличиваем счетчик его голов
                players[scored_player][3][goal_time] += 1  # увеличиваем счетчик голов игрока на минуте goal_time
                if i == 0:  # если текущий гол - первый гол команды в матче, обновляем first_goal_team2 и time_first_goal_team2
                    first_goal_team2, time_first_goal_team2 = scored_player, goal_time
            # обновляем счетчик открытия счета для команды и игрока
            if score1 > 0 and score2 > 0:  # если обе команды открыли счет
                if time_first_goal_team1 < time_first_goal_team2:  # если первая команда открыла счет раньше
                    teams[team1][2] += 1  # увеличиваем счетчик открытия счета в матчах для первой команды
                    players[first_goal_team1][2] += 1  # увеличиваем счетчик открытия счета в матчах для игрока забившего этот мяч
                else:  # иначе, если вторая команда открыла счет раньше
                    teams[team2][2] += 1  # увеличиваем счетчик открытия счета в матчах для второй команды
                    players[first_goal_team2][2] += 1  # увеличиваем счетчик открытия счета в матчах для игрока забившего этот мяч
            elif score1 > 0:  # если у команды 1 есть забитые мячи, а у команды 2 нет
                teams[team1][2] += 1  # увеличиваем счетчик открытия счета в матчах для первой команды
                players[first_goal_team1][2] += 1  # увеличиваем счетчик открытия счета в матчах для игрока забившего этот мяч
            elif score2 > 0:  # если у команды 2 есть забитые мячи, а у команды 1 нет
                teams[team2][2] += 1  # увеличиваем счетчик открытия счета в матчах для второй команды
                players[first_goal_team2][2] += 1  # увеличиваем счетчик открытия счета в матчах для игрока забившего этот мяч

        line = f.readline().strip()  # считываем следующую строку файла
# ответ
print(*answer, sep='\n')