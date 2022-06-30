import pandas as pd

def transactionMain(data, call):

    #looking for the positive only
    if(call == 1):
        data = data.loc[data['Net Amount (USD)'] > 0]
    #looking for the negative only    
    elif(call == 2):
        data = data.loc[data['Net Amount (USD)'] < 0]
    #looking for both the positive and negative

    return (data)
