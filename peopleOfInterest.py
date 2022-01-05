#!/usr/bin/python
# -*- coding: utf-8 -*-
from functools import total_ordering
import plotly.express as px
import pandas as pd
import csv
data = pd.read_csv('Community/Data.csv')


def poiMain():
    (data['totalExpense'], data['totalContribution']) = ('', '')
    data['Net Amount (USD)'] = round(data['Net Amount (USD)'
            ].astype(float), 2)
    dataCreation()


def dataCreation():
    for elem in range(0, len(data['User Profile'])):
        if data['totalExpense'][elem] == '':
            getAllExpenses('User Profile')


def getAllExpenses(name):
    expense = 0
    contribution = 0
    for elem in range(len(data['User Profile'])):
        if data['User Profile'][elem] != name:
            continue
        displayname = data['User Name'][elem]
        if data['Net Amount (USD)'][elem] < 0:
            expense = +round(data['Net Amount (USD)'][elem], 2)
        else:
            contribution = +round(data['Net Amount (USD)'][elem], 2)


def createGraph():
    poiData = pd.read_csv('Community/toolData/poiData.csv')
    fig = px.bar(poiData, x=poiData['Name'], y=(poiData['totalExpense'
                 ], poiData['totalContribution']))
    fig.show()


def main():
    poiMain()


if __name__ == '__main__':
    main()
