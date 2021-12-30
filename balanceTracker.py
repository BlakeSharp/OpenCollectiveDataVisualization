import pandas as pd

def balanceMain():
    data = pd.read_csv('Community/Data.csv')
    for elem in data['Transaction Description']:
        if('contribution' not in elem):
            print(elem)
    print('running balance')

balanceMain()