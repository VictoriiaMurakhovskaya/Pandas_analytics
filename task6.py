from service import write_to_excel, correl


def runtask(df, window):
    df.loc[df['Gender'] == 'male', 'GenderCode'] = 1
    df.loc[df['Gender'] == 'female', 'GenderCode'] = 2

    answers = [correl(df, 'Annual Income (x1000 $)', 'GenderCode')]
    titles = ['Annual income with Gender correlation']
    write_to_excel(titles, answers, 'Task 6')