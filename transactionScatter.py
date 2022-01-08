import plotly.express as px
import pandas as pd
import datetime

data = pd.read_csv('Community/Data.csv')
data['Net Amount (USD)'] = round(data['Net Amount (USD)'].astype(float),2)
editpos = data.loc[data['Net Amount (USD)'] > 0]
editneg = data.loc[data['Net Amount (USD)'] < 0]

for i in range(0,len(editpos['Order Date'])):
    try:
        editpos['Order Date'][i] = datetime.datetime.strptime(editpos['Order Date'][i].split('T')[0], "%Y-%m-%d")
    except:
        pass

for i in range(0,len(editneg['Order Date'])):
    try:
        editneg['Order Date'][i] = datetime.datetime.strptime(editneg['Order Date'][i].split('T')[0], "%Y-%m-%d")
    except:
        pass

def contributionMain():
    createGraph()

def createGraph():
    fig = px.scatter(editpos, x=editpos['Order Date'], y =(editpos['Net Amount (USD)']), hover_data=[editpos['User Name'],editpos['Transaction Description']], title="Net contributions per day (USD) over time", color=editpos['Net Amount (USD)'],range_color=[0, 1000])
    fig1 = px.scatter(editneg, x=editneg['Order Date'], y =(editneg['Net Amount (USD)']), hover_data=[editneg['User Name'],editneg['Transaction Description']], title="Net contributions per day (USD) over time", color=editneg['Net Amount (USD)'],range_color=[-10000, 0])
    fig.update_layout(hovermode="x unified")
    fig1.show()
    fig.show()


# this stops the import from running the script and allows from running direct from this file 

def main():
    contributionMain()

if __name__ == '__main__':
    main()