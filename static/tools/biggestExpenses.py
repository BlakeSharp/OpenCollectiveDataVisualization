import pandas as pd

def expensesMain(data):
    people = []
    data = data.loc[data['Net Amount (USD)'] < 0]
    data = data.groupby(by="User Name").sum()
    data = data.sort_values(by=['Net Amount (USD)'], ascending=False)

    return data.head(n=10)