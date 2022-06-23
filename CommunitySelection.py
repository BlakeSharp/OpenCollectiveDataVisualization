import tkinter as tk
from tkinter import Label, messagebox, Button
import pandas as pd
import os
from tools.balanceTracker import *
from tools.ContributionPerDay import *
from tools.expensePerDay import *
from tools.transactionScatter import *

# from TopDonators import donatorMain
# from TopPaid import paidMain
# this is the url for webpack which we should change with the thing the user wants
# https://opencollective.com/webpack/transactions?kind=CONTRIBUTION,EXPENSE
def Everything():
    balanceMain()
    contributionMain()
    expensesMain()
    transactionScatterMain()


def toolButtons():
    checkFileButton.destroy()

    # button initialization
    balanceGraphButton = Button(
        text="Balance", command=balanceMain, relief="raised"
    )
    contributionsButton = Button(
        text="Contributions", command=contributionMain, relief="raised",bg='#EDF2F4'
    )
    expensesButton = Button(
        text="Expenses", command=expensesMain, relief="raised",bg='#EDF2F4'
    )
    transcationScatter = Button(
        text="All Transaction Scatter Plot",
        command=transactionScatterMain,
        relief="raised",
        bg='#EDF2F4'
    )
    allGraphs = Button(
        text="Open All Available Graphs", command=Everything, relief="raised"
    )

    # packing
    allGraphs.pack()
    transcationScatter.pack()
    expensesButton.pack()
    balanceGraphButton.pack()
    contributionsButton.pack()
    root.iconphoto(False, tk.PhotoImage(file="images/icon.png"))


def errorLabel():
    messagebox.showerror(
        "Error", "Couldn't locate Data.csv File. Check spelling and refer to Readme."
    )


def goodLabel():
    messagebox.showerror("Success", "Data.csv File located!")


def fileCheck():
    checkfiles = os.listdir("Community")
    if "Data.csv" in checkfiles:
        goodLabel()
        toolButtons()
    else:
        errorLabel()


root = tk.Tk()
root.resizable(False, False)
root.title("Open Collective Visualization")
root.iconphoto(False, tk.PhotoImage(file="images/icon.png"))
root.geometry("300x200")
root.configure(bg='#8D99AE')

checkFileButton = Button(
    root, text="Check for File", command=fileCheck, relief="raised"
)
checkFileButton.pack()


root.mainloop()
