import tkinter as tk
from tkinter import Label, Button
import pandas as pd

root = tk.Tk()
data = pd.read_csv('Data.csv')

root.title('({}) graph selection'.format(data['accountSlug'][0]))
root.geometry("300x200+10+20")
root.mainloop()