import tkinter as tk
from tkinter import Label, Button
import pandas as pd

root = tk.Tk()
data = pd.read_csv('Data.csv')
root.iconphoto(False, tk.PhotoImage(file='images/icon.png'))
root.title('({}) graph selection'.format(data['accountSlug'][0]))

def first():
    print('thing')
B = Button(root, text ="Hello", command = first)
root.mainloop()