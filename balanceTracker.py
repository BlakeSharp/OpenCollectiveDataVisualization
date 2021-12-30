import pandas as pd
import plotly.graph_objects as go

data = pd.read_csv('Community/Data.csv')
def balanceMain():
    data['Net Amount (USD)'] = round(data['Net Amount (USD)'].astype(float),2)
    for x in range(0, len(data['Transaction Description'])):
        if('contribution' not in data['Transaction Description'][x]):
            print(data['Transaction Description'][x] )
            print(data['Transaction Amount'][x])
            print(data['Net Amount (USD)'][x])
            print(data['User Name'][x])
            print("----------------------")
    data['Running Balance'] = data['Net Amount (USD)'][len(data['Net Amount (USD)'])-2]
    for x in reversed(range(0,(len(data['Net Amount (USD)']))-2)):
        data['Running Balance'][x] = (data['Net Amount (USD)'][x] + data['Running Balance'][x+1])
    data.to_csv("Data.csv", index=False)
    creatingGraph()



def creatingGraph():
    fig = go.Figure([go.Scatter(x=data['Transaction Date'], y=data['Running Balance'])])
    fig.show()


def main():
    balanceMain()

if __name__ == '__main__':
    main()