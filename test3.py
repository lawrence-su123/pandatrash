import os
import tkinter as tk
from tkinter import ttk

folder = 'C:/Users/lawre/Downloads'
filelist = [fname for fname in os.listdir(folder) if fname.endswith('.csv')]

master = tk.Tk()
master.geometry('1200x800')
master.title('Select a file')

optmenu = ttk.Combobox(master, values=filelist, state='readonly')
optmenu.pack(fill='x')

master.mainloop()