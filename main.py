import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from pandas import Series
import barplot as bp
import warnings
warnings.filterwarnings("ignore")


train = pd.read_csv("data/Train_SU63ISt.csv")
test = pd.read_csv("data/Test_0qrQsBZ.csv")


train_original = train.copy()
test_original = test.copy()

##########################################################################
# Exploratory Analysis
train['Datetime'] = pd.to_datetime(train.Datetime, format='%d-%m-%Y %H:%M')
test['Datetime'] = pd.to_datetime(test.Datetime, format='%d-%m-%Y %H:%M')
test_original['Datetime'] = pd.to_datetime(test_original.Datetime, format='%d-%m-%Y %H:%M')
train_original['Datetime'] = pd.to_datetime(train_original.Datetime, format='%d-%m-%Y %H:%M')

for i in (train, test, test_original, train_original):
    i['year'] = i.Datetime.dt.year
    i['month'] = i.Datetime.dt.month
    i['day'] = i.Datetime.dt.day
    i['Hour'] = i.Datetime.dt.hour

train['day of week'] = train['Datetime'].dt.dayofweek
temp = train['Datetime']

# This functions adds a boolean value 1 if the current day is a weekend


def is_weekend(row):
    if row.dayofweek == 5 or row.dayofweek == 6:
        return 1
    else:
        return 0


temp2 = train['Datetime'].apply(is_weekend)
train['weekend'] = temp2

# train.index = train['Datetime']  # indexing the Datetime to get the time period on the x-axis.
# df = train.drop('ID', 1)           # drop ID variable to get only the Datetime on x-axis.
# ts = df['Count']
# # plt.figure(figsize=(16, 8))
# # plt.plot(ts, label='Passenger Count')
# # plt.title('Time Series')
# # plt.xlabel("Time(year-month)")
# # plt.ylabel("Passenger count")
# # plt.legend(loc='best')
# # plt.show()
#
# temp_data = train.groupby('month')['Count'].mean()
# x_axis_data = temp_data.index
# y_axis_data = temp_data[:]
# bp.plot_bar_x(x_axis_data, y_axis_data, 'Month', 'Count', 'Monthly Count')
#######################################################################################
# Splitting and forecasting
train=train.drop('ID', 1)

test.Timestamp = pd.to_datetime(test.Datetime, format='%d-%m-%Y %H:%M')
test.index = test.Timestamp

# Converting to daily mean
test = test.resample('D').mean()

train.Timestamp = pd.to_datetime(train.Datetime, format='%d-%m-%Y %H:%M')
train.index = train.Timestamp

# Converting to daily mean
train = train.resample('D').mean()

Train = train.ix['2012-08-25':'2014-06-24']
valid = train.ix['2014-06-25':'2014-09-25']

Train.Count.plot(figsize=(15,8), title= 'Daily Ridership', fontsize=14, label='train')
valid.Count.plot(figsize=(15,8), title= 'Daily Ridership', fontsize=14, label='valid')
plt.xlabel("Datetime")
plt.ylabel("Passenger count")
plt.legend(loc='best')
plt.show()

