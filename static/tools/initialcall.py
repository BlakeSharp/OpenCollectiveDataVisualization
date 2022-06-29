import pandas as pd

data = pd.read_csv('Data.csv')


def Initialmain():
    data.drop('Transaction Description', 1 , inplace = True)
    data.drop('Tags', 1 , inplace = True)
    data.drop('Collective Currency', 1 , inplace = True)
    data.drop('Transaction Amount', 1 , inplace = True)
    data.drop('Host Fee (USD)', 1 , inplace = True)
    data.drop('Open Collective Fee (USD)', 1 , inplace = True)
    data.drop('Payment Processor Fee (USD)', 1 , inplace = True)
    data.drop('UserName', 1 , inplace = True)
    data.drop('User Name', 1 , inplace = True)



    data.to_csv('Data.csv')

def main():
    Initialmain()

if __name__ == "__main__":
    main()