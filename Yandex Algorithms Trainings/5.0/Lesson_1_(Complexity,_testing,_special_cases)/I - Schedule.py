from datetime import datetime

# считываем данные
N = int(input().strip())  # количество гос праздников
year = int(input().strip())  # год
holidays = [''] * N  # список гос праздников
for i in range(N):
    day, month = input().split()  # день праздника, месяц праздника
    day = int(day)
    holidays[i] = (day, month)

start_weekday = input().strip()  # день недели начала года
# словари дней недели
weekdays_to_int = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4,
            'Friday': 5, 'Saturday': 6, 'Sunday': 7}
int_to_weekdays = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday',
            5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
weekday_diff = datetime(year, 1, 1).weekday() - weekdays_to_int[start_weekday]  # разница дней недели между заданным и datetime
days_arr = [-1] + [52] * 7  # массив дней недели
days_arr[weekdays_to_int[start_weekday]] += 1  # увеличиваем начальный день недели в массиве days_arr для 365 дней
end_weekday = (datetime(year, 12, 31).weekday() - weekday_diff) % 7  # день недели окончания года
end_weekday = end_weekday if end_weekday != 0 else 7
# если день недели начала года не совпадает с днем недели окончания года - увеличиваем в days_arr счетчик дня недели окончания года
if end_weekday != weekdays_to_int[start_weekday]:
    days_arr[end_weekday] += 1
# словарь месяцев
months = {'January': 1, 'February': 2, 'March': 3, 'April': 4,
          'May': 5, 'June': 6, 'July': 7, 'August': 8,
          'September': 9, 'October': 10, 'November': 11, 'December': 12}
# проходим по праздникам - уменьшаем счетчик дней в days_arr
for day, month in holidays:
    weekday = (datetime(year, months[month], day).weekday() - weekday_diff) % 7
    weekday = weekday if weekday != 0 else 7
    days_arr[weekday] -= 1

best_weekday = days_arr.index((max(days_arr[1:])))  # лучший день недели для выходного
worse_weekday = days_arr.index((min(days_arr[1:])))  # худший день недели для выходного
# ответ
print(int_to_weekdays[best_weekday], int_to_weekdays[worse_weekday])
