import tkinter as tk
from tkinter import Label, messagebox
import requests
import csv
#this is the url for webpack which we should change with the thing the user wants
#https://rest.opencollective.com/v2/webpack/transactions.txt?kind=CONTRIBUTION%2CEXPENSE%2CHOST_FEE%2CPAYMENT_PROCESSOR_COVER&includeGiftCardTransactions=1&includeIncognitoTransactions=1&includeChildrenTransactions=1


root= tk.Tk()
root.geometry('500x300')
root.resizable(False,False)
root.title('Open Collective Visualization')

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

NameEntry = tk.Entry (root) 
canvas1.create_window(200, 140, window=NameEntry)
def errorLabel():
    messagebox.showerror('Error','There was an error requesting data. Please check spelling and try again.')

    

def getFile ():  
    Name = NameEntry.get()
    Name = Name.strip().lower()
    url = 'https://rest.opencollective.com/v2/{}/transactions.txt?kind=CONTRIBUTION%2CEXPENSE%2CHOST_FEE%2CPAYMENT_PROCESSOR_COVER&includeGiftCardTransactions=1&includeIncognitoTransactions=1&includeChildrenTransactions=1'.format(Name)
    r = requests.get(url, allow_redirects=True)
    open('Data.csv', 'wb').write(r.content)
    r.close() 
    file = open('Data.csv').readlines()
    if(str(file[0])[:10]!='"datetime"'):
        errorLabel()
    
findDataButton = tk.Button(text='Find', command=getFile)
canvas1.create_window(200, 180, window=findDataButton)

root.mainloop()