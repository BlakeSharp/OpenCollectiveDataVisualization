#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

data = pd.read_csv('Community/Data.csv')


def balanceMain():

    # changed every row in the column 'Net Amont (USD)' to a float value

    data['Net Amount (USD)'] = round(data['Net Amount (USD)'
            ].astype(float), 2)

    # Creates a column for running balance and sets each value to the last so that it can be traversed backwards (most likely a better way to do this)

    data['Running Balance'] = data['Net Amount (USD)'
                                   ][len(data['Net Amount (USD)']) - 1]

    # traverse a list of numbers from the len -> 0 adding each value x from the on before it (which is the other after it in the list so x+1)

    for x in reversed(range(0, len(data['Net Amount (USD)']) - 2)):
        data['Running Balance'][x] = round(data['Net Amount (USD)'][x]
                + data['Running Balance'][x + 1], 2)

    # save csv

    data.to_csv('Community/Data.csv', index=False)

    return(
        go.Figure([go.Scatter(x=data['Transaction Date'],
                    y=data['Running Balance'])])
                    )


def main():
    balanceMain()


if __name__ == '__main__':
    main()