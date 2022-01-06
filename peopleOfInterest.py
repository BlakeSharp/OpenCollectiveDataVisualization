#!/usr/bin/python
# -*- coding: utf-8 -*-
from functools import total_ordering
import plotly.express as px
import pandas as pd


data = pd.read_csv('Community/Data.csv')
data['Net Amount (USD)'] = round(data['Net Amount (USD)'].astype(float),2)
data['UserName'] = pd.NaT
length = len(data['User Name'])
for elem in range(0, length):
    (data['UserName'][elem]) = data['User Name'][elem]
data.to_csv('Community/Data.csv', index=False)

newdata = pd.read_csv('Community/Data.csv')
for elem in newdata.head():
    print(elem)

contributions = newdata.loc[newdata['Net Amount (USD)'] > 0]
expenses = newdata.loc[newdata['Net Amount (USD)'] < 0]

def poiMain():
    totalContributions = contributions.groupby('User Profile').sum()
    totalExpenses = expenses.groupby('User Profile').sum()
    for elem in totalExpenses.head():
        print(elem)
    conLength = len(totalContributions['UserName'])
    for elem in totalContributions.head():
        print(elem)
    for elem in range(0,conLength):
        print(totalContributions['Net Amount (USD)'])




def main():
    poiMain()


if __name__ == '__main__':
    main()
