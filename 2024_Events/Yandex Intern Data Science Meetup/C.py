# OK
# так как по условиям задачи не сказано что FP постоянно изменяется, тогда
# при увеличении TP до 100 и неизменении FP в 40, ответ 0,833333

# max_f_score при равномерном изменении TP и FP
max_f_score = 0
for TP in range(40, 101):
    FP = max(0, TP - 40)
    FN = 100 - TP
    TN = 100 - FP

    PR = TP / (TP + FP)
    RC = TP / (TP + FN)
    print('точность', PR, 'полнота', RC)
    max_f_score = max(round(2 * TP/(2 * TP + FP + FN), 6), max_f_score)
    print('TP', TP, 'f-score-1', 2 * TP/(2 * TP + FP + FN))
    print('TP', TP, 'f-score-2', (2 * PR * RC) / (PR + RC))

print(max_f_score)