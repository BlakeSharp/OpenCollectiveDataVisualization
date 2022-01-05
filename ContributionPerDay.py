import plotly.express as px
import pandas as pd

data = pd.read_csv('Community/Data.csv')
data['Net Amount (USD)'] = round(data['Net Amount (USD)'].astype(float),2)
edit = data.loc[data['Net Amount (USD)'] > 0]


def contributionMain():
    createGraph()

def createGraph():
    fig = px.line(edit, x=edit['Transaction Date'], y=edit['Net Amount (USD)'])
    fig.show()

def main():
    contributionMain()

if __name__ == '__main__':
    main()