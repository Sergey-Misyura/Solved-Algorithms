import numpy as np
from scipy import stats

# Количество симуляций
num_simulations = 10000
# Количество дней
num_days = 30
# Количество слушателей в каждом зале
num_listeners = 5000
# Уровень значимости
alpha = 0.05
# Счетчик для случаев, когда нулевая гипотеза отвергается
false_positives = 0

for _ in range(num_simulations):
    for day in range(num_days):
        # Генерация случайных ответов слушателей
        # 1 - понравилось, 0 - не понравилось
        responses_a = np.random.binomial(1, 0.5, num_listeners)
        responses_b = np.random.binomial(1, 0.5, num_listeners)
        # Вычисление p-value
        _, p_value = stats.ttest_ind(responses_a, responses_b)
        # Проверка p-value
        if p_value < alpha:
            false_positives += 1
            break

# Расчет доли случаев, когда нулевая гипотеза была отвергнута
error_rate = false_positives / num_simulations

print(f"Реальная ошибка первого рода: {error_rate}")
# ответ 28 %