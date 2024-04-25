import pandas as pd
from datetime import datetime, timedelta

def process(df):  # функция возвращает сумму вклада за 02.2024 трех топовых подписчиков
    df['mean'] = df['billing_total_price_usd'] / df['billing_period']  # вклад подпиской за 1 день
    feb_start = datetime.strptime("31012024", "%d%m%Y")  # граница периода перед началом 02.2024
    feb_end = datetime.strptime("01032024", "%d%m%Y")  # граница периода после конца 02.2024
    df['timestamp'] = pd.to_datetime(df.timestamp, unit='s').dt.normalize()  # преобразование timestamp в datetime
    df['billing_period'] = pd.to_timedelta(df.billing_period, unit='D')  # преобразование оплачиваемого периода в timedelta
    df['end_period'] = df['timestamp'] + df['billing_period']  # последний день оплачиваемого периода
    df['start_period'] = df['timestamp'].apply(lambda x: max(x, feb_start))  # левая граница пересечения периода подписки с границей 02.2024
    df['end_period'] = df['end_period'].apply(lambda x: min(x, feb_end))  # правая граница пересечения периода подписки с границей 02.2024
    df['days_delta'] = df['end_period'] - df['start_period']  # количество дней вносящих вклад за 02.2024
    # для периодов лежащих внутри 02.2024 расчет дней внесящих вклад в феврале верен
    # а для периодов с границами feb_start или feb_end необходимо вычесть 1 день вносящий средства, так как не учитываются неполные сутки
    # для полностью попадающего февраля также вычитается 1 день - убираются лишний раз учтенные полные сутки
    df.loc[(df['start_period'] == feb_start) | (df['end_period'] == feb_end), 'days_delta'] -= timedelta(days=1)
    df['days_delta'] = df['days_delta'].mask(df['days_delta'] < timedelta(0), timedelta(0))  # замена отрицательных days_delta на 0

    df['income'] = df['days_delta'].dt.days * df['mean']  # вносимый вклад в феврале каждым платежем
    top_3_users = df[['user_id', 'income']].groupby(by=["user_id"]).sum().sort_values(by='income', ascending=False)  # группировка income по пользователям
    # возвращем сумму вкладов в феврале топ 3 пользователей по вкладу
    return top_3_users['income'].head(3).sum().round(2)

# проверка функции
df = pd.read_csv("sample_1.csv")
print(process(df))