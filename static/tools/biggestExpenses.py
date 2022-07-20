import pandas as pd

def expensesMain(data):
    data = data.loc[data['Net Amount (USD)'] < 0]
    data = data.groupby("User Name")["Transaction Amount"].sum().sort_values(ascending=True)
    return data.head(n=10) 

