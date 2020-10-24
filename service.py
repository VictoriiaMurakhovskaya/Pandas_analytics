import pandas as pd
from tkinter import filedialog as fd
from openpyxl import load_workbook
import os
from math import sqrt


def write_to_excel(questions, answers, sheetname):
    answer = pd.DataFrame({'Questions': questions, 'Answers': answers})

    filename = fd.asksaveasfilename(defaultextension='.xlsx',
                                    filetypes=[('MS Excel files', '*.xlsx')])
    if os.path.exists(filename):
        book = load_workbook(filename)
    writer = pd.ExcelWriter(filename, engine='openpyxl')

    try:
        writer.book = book
    except:
        pass
    answer.to_excel(writer, sheet_name=sheetname, index=False)
    writer.save()
    writer.close()


def correl(df, col1, col2):
    df['x'] = df[col1] - df[col1].mean()
    df['y'] = df[col2] - df[col2].mean()
    df['cum'] = df['x'] * df['y']
    df['x2'] = df['x'] * df['x']
    df['y2'] = df['y'] * df['y']
    return df['cum'].sum() / sqrt(df['x2'].sum() * df['y2'].sum())


def numerical_key(df, column):
    values = df[column].unique()
    for item in enumerate(values):
        df.loc[df[column] == item[1], column+'(code)'] = item[0]
    return df