from tkinter import filedialog as fd
import pandas as pd


def runtask(df, window):
    df['Annual spendings on electronics'] = 12 * df['Monthly Electronics Spend']
    df['Spendings as % of income'] = df['Annual spendings on electronics'] / df['Annual Income (x1000 $)'] / 10

    filename = fd.asksaveasfilename(defaultextension='.xlsx',
                                    filetypes=[('MS Excel files', '*.xlsx')])

    writer = pd.ExcelWriter(filename, engine='openpyxl')

    df.to_excel(writer, sheet_name='Task 2', index=False)
    writer.save()
    writer.close()