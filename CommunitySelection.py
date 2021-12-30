import tkinter as tk
from tkinter import Label, messagebox, Button
from tkinter.constants import E
import requests
import csv
#from balanceTracker import balanceMain
import pandas as pd
import os
#from TopDonators import donatorMain
#from TopPaid import paidMain
#this is the url for webpack which we should change with the thing the user wants
#https://opencollective.com/webpack/transactions?kind=CONTRIBUTION%2CEXPENSE


root= tk.Tk()
root.resizable(False,False)
root.title('Open Collective Visualization')
root.iconphoto(False, tk.PhotoImage(file='images/icon.png'))

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

findDataButton = Button(text='GET DATA', command=getFile, bg='#79869c', relief='raised')
NameEntry = tk.Entry (root) 
canvas1.create_window(200, 140, window=NameEntry)

def errorLabel():
    messagebox.showerror('Error','There was an error requesting data. Please check spelling and try again.')

def graphSelectionScreen():
    NameEntry.destroy()
    findDataButton.destroy()
    balanceGraphButton = Button(text='Balance Over Time', command=balanceMain(), relief='raised')
    balanceGraphButton.pack()
    topPaidButton = Button(text='Most expense', command=paidMain(), relief='raised')
    topPaidButton.pack()
    topDonatorButton = Button(text='Top Donators', command=donatorMain(), relief='raised')
    topDonatorButton.pack()
    emptyButton = Button(text='Balance', command=balanceMain(), relief='raised')
    emptyButton.pack()
    data = pd.read_csv('Data.csv')
    root.iconphoto(False, tk.PhotoImage(file='images/icon.png'))
    root.title('({}) graph selection'.format(data['accountSlug'][0]))
    canvas1.destroy()

 
canvas1.create_window(200, 180, window=findDataButton)

root.mainloop()