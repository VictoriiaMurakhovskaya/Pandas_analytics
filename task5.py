from service import write_to_excel, correl


def runtask(df, window):
    answers = [correl(df, 'Annual Income (x1000 $)', 'Age')]
    titles = ['Annual income with Age correlation']
    write_to_excel(titles, answers, 'Task 5')