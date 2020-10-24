from tkinter import Frame, Toplevel, TOP, LEFT, Button, NO
from tkinter.ttk import Treeview, Combobox
from graphs import show_graph


def get_choice(df):
    return [item for item in df]


def runtask(df, window):
    global attributes, parentwindow
    parentwindow = window

    showbox = Toplevel(window)
    showbox.geometry("220x210")


    attributes = Combobox(showbox, values=get_choice(df), width=28)
    attributes.pack(side=TOP, padx=10, pady=(10, 5))
    attributes.current(0)

    headings = {'Attribute': 100, 'Value': 40, '%': 40}
    result = Treeview(showbox)
    result['columns'] = list(headings.keys())
    result.column('#0', width=8, minwidth=5, stretch=NO)
    for column in headings:
        result.column(column, width=headings[column])
        result.heading(column, text=column)
    result.config(height=5)
    result.pack(side=TOP)

    buttons = Frame(showbox)
    Button(buttons, text='Graph', width=11, command=lambda x=df: launch_graph(x)).pack(side=LEFT, padx=(10, 5))
    Button(buttons, text='Close', width=11, command=showbox.destroy).pack(side=LEFT, padx=(0, 10))
    buttons.pack(side=TOP, padx=10, pady=(10, 10))

    attributes.bind('<<ComboboxSelected>>', lambda event, table=result, data=df: change_attribute(event, table, data))
    fill_result(result, df, attributes.get())


def launch_graph(df):
    col_name = attributes.get()
    y = make_df(df, col_name)
    headings = [item for item in y]
    x = y[headings[0]]
    y = y[headings[-1]]
    show_graph(x, y, 'bar', parentwindow, 'Percentage for responses for each answer')


def make_df(df, col_name):
    # calculate result
    y = df[col_name].value_counts().reset_index()
    y.columns = [col_name, 'count']
    total = sum(y['count'])
    y['percentage'] = y['count']/total*100
    return y


def change_attribute(event, table, df):
    fill_result(table, df, event.widget.get())


def fill_result(table, df, col_name):
    # clear result table
    x = table.get_children()
    for item in x:
        table.delete(item)
    y = make_df(df, col_name)
    for index, row in y.iterrows():
        table.insert('', index, values=tuple([str(item) for item in row]))


