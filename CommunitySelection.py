import tkinter as tk
from tkinter import Label, messagebox, Button
#from balanceTracker import balanceMain
import pandas as pd
import os
from balanceTracker import *
from peopleOfInterest import *
from ContributionPerDay import *
from expensePerDay import *
#from TopDonators import donatorMain
#from TopPaid import paidMain
#this is the url for webpack which we should change with the thing the user wants
#https://opencollective.com/webpack/transactions?kind=CONTRIBUTION%2CEXPENSE

def toolButtons():
    checkFileButton.destroy()
    balanceGraphButton = Button(text='Balance Over Time', command=balanceMain, relief='raised')
    balanceGraphButton.pack()
    topPaidButton = Button(text='Most expense', command=poiMain, relief='raised')
    topPaidButton.pack()
    topDonatorButton = Button(text='Top Donators', command=poiMain, relief='raised')
    topDonatorButton.pack()
    contributionsButton = Button(text='Contributions Over Time', command=contributionMain, relief='raised')
    contributionsButton.pack()
    expensesButton = Button(text='Contributions Over Time', command=expensesMain, relief='raised')
    expensesButton.pack()
    root.iconphoto(False, tk.PhotoImage(file='images/icon.png'))
    root.title('({}) graph selection'.format(data['accountSlug'][0]))


def errorLabel():
    messagebox.showerror('Error',"Couldn't locate Data.csv File. Check spelling and refer to Readme.")
def goodLabel():
    messagebox.showerror('Success',"Data.csv File located!")

def fileCheck():
    checkfiles = os.listdir('Community')
    if 'Data.csv' in checkfiles:
        goodLabel()
        toolButtons()
    else: 
        errorLabel()

root= tk.Tk()
root.resizable(False,False)
root.title('Open Collective Visualization')
root.iconphoto(False, tk.PhotoImage(file='images/icon.png'))
root.geometry('300x200')



checkFileButton = Button(root, text='Check for File', command=fileCheck, relief='raised')
checkFileButton.pack()




root.mainloop()