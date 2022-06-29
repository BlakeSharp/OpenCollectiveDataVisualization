import pandas as pd

def transactionMain(call):
    data = pd.read_csv('Data.csv')

    #looking for the positive only
    if(call == 1):
        data = data.loc[data['Net Amount (USD)'] > 0]
    #looking for the negative only    
    elif(call == 2):
        data = data.loc[data['Net Amount (USD)'] < 0]
    #looking for both the positive and negative

    return (data['Net Amount (USD)'])


print(transactionMain(0))