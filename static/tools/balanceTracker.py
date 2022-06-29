#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


#.iloc[::-1] reverses the rows in the data frame making it oldest -> newest, allowing for cumulative sum to be used to 
# accuratly track the the running balance of all transactions
data = pd.read_csv('Data.csv'
            ).iloc[::-1]

def balanceMain():

    # changed every row in the column 'Net Amont (USD)' to a float value

    data['Net Amount (USD)'] = round(data['Net Amount (USD)'
            ].astype(float), 2)



    #This creates 'Running Balance' as the last column in the dataframe and set each cell equal to the cumuliative sum
    #of the value of 'Net Amount (USD)' (this works because the rows are reversed by the initial .iloc when reading data.csv)
    data['Running Balance'] = data['Net Amount (USD)'].cumsum()

    
    #.iloc[::-1] revereses the order of the rows of the dataframe again, reverting back to the newest -> oldest order
    
    #save csv
    data.iloc[::-1].to_csv('Data.csv', index=False)


def main():
    balanceMain()


if __name__ == '__main__':
    main()