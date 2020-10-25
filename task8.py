import pandas as pd
import itertools as it
from tkinter import filedialog as fd
import os
from openpyxl import load_workbook


segments = ['Gender', 'Education']


def runtask(df, window):
    # segmentation
    lst1 = df[segments[0]].unique()
    lst2 = df[segments[1]].unique()
    index = ['Market size', 'Average income', 'Description of segment', 'Most feature', 'Shopped stores',
             'Avg. el. purchase']
    seg_columns = {}
    for item in it.product(lst1, lst2):
        val = []
        # segment data selection
        y = df.loc[(df[segments[0]] == item[0]) & (df[segments[1]] == item[1])]
        val.append(len(y.index))
        val.append(y['Annual Income (x1000 $)'].mean())
        val.append(item)
        z = y['Favorite feature'].value_counts().reset_index()
        val.append(z.at[0, 'index'])
        z = y['Purchasing Location'].value_counts().reset_index()
        val.append(z.at[0, 'index'])
        val.append(y['Monthly Electronics Spend'].mean())
        seg_columns.update({item: val})
    answer = pd.DataFrame(seg_columns, index=index)

    df['Age Segment'] = pd.cut(df['Age'], 4, right=True)
    seg_columns = {}
    for item in sorted(list(df['Age Segment'].unique())):
        val = []
        # segment data selection
        y = df.loc[df['Age Segment'] == item]
        val.append(len(y.index))
        val.append(y['Annual Income (x1000 $)'].mean())
        val.append(item)
        z = y['Favorite feature'].value_counts().reset_index()
        val.append(z.at[0, 'index'])
        z = y['Purchasing Location'].value_counts().reset_index()
        val.append(z.at[0, 'index'])
        val.append(y['Monthly Electronics Spend'].mean())
        seg_columns.update({item: val})

    answer2 = pd.DataFrame(seg_columns, index=index)

    filename = fd.asksaveasfilename(defaultextension='.xlsx',
                                    filetypes=[('MS Excel files', '*.xlsx')])

    writer = pd.ExcelWriter(filename, engine='openpyxl')

    answer.to_excel(writer, sheet_name='Segmentation 1', index=True)
    answer2.to_excel(writer, sheet_name='Segmentation 2', index=True)
    writer.save()
    writer.close()





