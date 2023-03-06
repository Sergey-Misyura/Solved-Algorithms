time_A = input()
time_B = input()
time_C = input()


def time_in_sec(time):
    h, m, s = map(int, time.split(':'))
    return (h * 60 + m) * 60 + s


time_A = time_in_sec(time_A)
time_B = time_in_sec(time_B)
time_C = time_in_sec(time_C)
delay = (time_C - time_A) / 2
delay = int(delay) + 1 if delay - int(delay) == 0.5 else round(delay)
output_time = time_B + delay

h = output_time // 3600
m = (output_time - h * 3600) // 60
s = (output_time - h * 3600) - m * 60
h = h % 24

print(f'{h}:{m}:{s}')