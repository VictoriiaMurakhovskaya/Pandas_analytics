from tkinter import Tk, Entry, Label, Button, Frame, LEFT, TOP, StringVar
from tkinter.ttk import Combobox
from tkinter import filedialog as fd
from tkinter import PhotoImage as pim
import xlrd
import configparser
import os
from importlib import import_module
import pandas as pd

tsk_list = ['Task #{!s}'.format(i) for i in range(2, 10)]
df = pd.DataFrame()


def choosefile():
    global file
    file.set(fd.askopenfilename(defaultextension='.xlsx',
                                filetypes=[('MS Excel files', '*.xlsx')]))
    sheets_list()


def sheets_list():
    global sheets
    if os.path.exists(file.get()):
        wb = xlrd.open_workbook(file.get())
        sheets['values'] = wb.sheet_names()
        if not sheets.get():
            sheets.current(1)


def on_load():
    global file
    if os.path.exists('config.cfg'):
        config = configparser.ConfigParser()
        config.read('config.cfg')
        try:
            file.set(config.get("Files", "main"))
            sheets.set(config.get("Files", "sheet"))
        except:
            pass
    sheets_list()


def on_closing(w):
    global file
    config = configparser.ConfigParser()
    config.add_section("Files")
    config.set("Files", "main", file.get())
    config.set("Files", "sheet", sheets.get())
    with open('config.cfg', "w") as config_file:
        config.write(config_file)
    w.destroy()


def load_df():
    global df
    df = pd.read_excel(file.get(), sheet_name=sheets.get(), index_col=0)


def run_task():
    if df.empty:
        load_df()
    num = tasks.current()
    name = 'task'+str(num + 2)
    module = import_module(name, package=__name__)
    module.runtask(df, window)


def ui():
    global file, sheets, tasks, window
    window = Tk()
    pixelVirtual = pim(width=1, height=1)
    window.geometry("280x105")
    window.title('Pandas')
    file = StringVar(window)
    labels = Frame(window)
    entries = Frame(window)
    buttons = Frame(window)
    Label(labels, text='Data files').pack(side=TOP, padx=(10, 5), pady=(10, 3))
    Label(labels, text='Survey data').pack(side=TOP, padx=(10, 5), pady=3)
    Label(labels, text='Tasks choice').pack(side=TOP, padx=(10, 5), pady=3)
    Entry(entries, textvariable=file, width=25).pack(side=TOP, pady=(10, 3))
    sheets = Combobox(entries, values=[], width=22)
    sheets.pack(side=TOP, pady=3)
    tasks = Combobox(entries, values=tsk_list, width=22)
    tasks.pack(side=TOP, pady=3)
    tasks.current(0)
    Button(buttons, text='...', image=pixelVirtual, height=12, command=choosefile, compound='c').pack(side=TOP, padx=(10, 5), pady=(10, 3))
    Button(buttons, text='...', image=pixelVirtual, height=12, command=load_df, compound='c').pack(side=TOP, padx=(10, 5), pady=3)
    Button(buttons, text='...', image=pixelVirtual, height=12, command=run_task, compound='c').pack(side=TOP, padx=(10, 5), pady=3)
    labels.pack(side=LEFT)
    entries.pack(side=LEFT)
    buttons.pack(side=LEFT)
    on_load()
    window.protocol("WM_DELETE_WINDOW", lambda f=window: on_closing(f))
    window.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ui()
