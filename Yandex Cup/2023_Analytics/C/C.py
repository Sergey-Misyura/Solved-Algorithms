import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('path2.csv')  # cleared path
data.plot.line(x='x', y='y', style='-o')
plt.show()

total = 0
for i in range(len(data)-1):
    total += ((data.iloc[i][0]-data.iloc[i+1][0])**2 + (data.iloc[i][1]-data.iloc[i+1][1])**2)**0.5


print(total) # answer 3.18015