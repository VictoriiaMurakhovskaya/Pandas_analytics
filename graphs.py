from tkinter import Toplevel, BOTH, BOTTOM
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


def show_graph(x, y, type, window, title):
    graph = Toplevel(window)
    graph.title('Graphic view')
    graph.minsize(width=400, height=200)

    fig = Figure(figsize=(5, 4), dpi=100)
    fig.clear()
    ax = fig.subplots()
    rects1 = ax.bar(x, y)
    autolabel(rects1, ax, True)
    ax.set_title(title)
    ax.set_ylim([0, max(list(y)) * 1.2])
    fig.autofmt_xdate()
    canvas = FigureCanvasTkAgg(fig, master=graph)
    canvas.draw()
    canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, graph)
    toolbar.update()
    canvas.get_tk_widget().pack(fill=BOTH, expand=1)


def autolabel(rects, ax, per_flag):
    """ autoticker for diagram """
    for rect in rects:
        height = rect.get_height()
        ax.annotate(('{:d}' + ' %' if per_flag else '').format(int(height) if height > 0 else 0),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')