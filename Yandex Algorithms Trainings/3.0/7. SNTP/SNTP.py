time_A = input()
time_B = input()
time_C = input()

def time_in_sec(time):
    h,m,s = map(int, time.split(':'))
    return (h*60+m)*60+s

def time_to_str(time):
	time = str(time) if time > 9 else '0'+str(time)
	return time
   
time_A, time_C = time_in_sec(time_A), time_in_sec(time_C)
time_C += 24*3600 if time_A > time_C else 0
delay = (time_C - time_A)/2
delay = int(delay)+1 if delay - int(delay) == 0.5 else round(delay)
output_time = time_in_sec(time_B) + delay

h = output_time // 3600
m = (output_time - h*3600)//60
s = (output_time - h*3600) - m*60
h = h % 24
output = time_to_str(h)+':'+time_to_str(m)+':'+time_to_str(s)
print(output)