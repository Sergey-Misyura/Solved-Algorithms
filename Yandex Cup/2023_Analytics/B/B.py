import pandas as pd
import numpy as np
from datetime import timedelta

data = pd.read_csv('startup_users_visits.csv')
data.sort_values('date', inplace=True)  # sort by date
data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d')  # values to datetime
data.index = pd.to_datetime(data['date'], format='%Y-%m-%d')

days_90 = timedelta(days=90)  # add timedelta
uniq_id = set()  # set of seen id's
answer_df = data.head(0)  # new cleared df

for row in data.iterrows():
    cur_id = row[1]['user_id']
    if cur_id not in uniq_id:  # check every new id
        date = row[1]['date']
        data_90_days = data[(data['date'].between(date, date + days_90)) & (data['pay'] == True)]
        if cur_id in data_90_days['user_id'].values:
            answer_df = answer_df.append(row[1])  # add row to answer df if new and paid within 90 days
        uniq_id.add(cur_id)  # add to seen id's set

# count of persons grouped by month
count_df = answer_df['date'].groupby(answer_df.date.dt.to_period("M")).agg('count')
print(count_df)
count_df.to_csv('answer.csv')

# in answer.csv delete header and last 3 rows by condition, add to date col first day of month '-01'
