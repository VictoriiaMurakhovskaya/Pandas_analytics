import pandas as pd
from tkinter import filedialog as fd

categories = {'Demographic': ['Gender', 'Marital Status', 'Work Status', 'Education', 'Annual Income (x1000 $)',
                              'Age', 'Location'],
              'Purchasing': ['Purchasing Decision-maker', 'Purchasing Location'],
              'Behavioral': ['Monthly Electronics Spend', 'Monthly Household Spend',
                             'Purchasing Frequency (every x months)'],
              'Attitude': ['Technology Adoption', 'TV Viewing (hours/day)'],
              'Other': ['Favorite feature']}

datafield, segmentation_param = [], []


def runtask(df, window):
    for key in categories.keys():
        for item in categories[key]:
            segmentation_param.append(key)
            datafield.append(item)

    answer = pd.DataFrame({'Segmentation parameter': segmentation_param, 'Data field': datafield})

    filename = fd.asksaveasfilename(defaultextension='.xlsx',
                                    filetypes=[('MS Excel files', '*.xlsx')])

    writer = pd.ExcelWriter(filename, engine='openpyxl')

    answer.to_excel(writer, sheet_name='Task 1', index=False)
    writer.save()
    writer.close()