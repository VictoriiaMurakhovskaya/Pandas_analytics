from service import write_to_excel, correl, numerical_key


def runtask(df, window):
    df = numerical_key(df, 'Education')
    df = numerical_key(df, 'Favorite feature')
    answers = [correl(df, 'Age', 'Purchasing Frequency (every x months)'),
               correl(df, 'Annual Income (x1000 $)', 'TV Viewing (hours/day)'),
               correl(df, 'Education(code)', 'Favorite feature(code)'),
               correl(df, 'Monthly Electronics Spend', 'Monthly Household Spend')]
    titles = ['Age and Purchasing Frequency', 'Annual Income and TV Viewing', 'Education and Favorite feature',
              'Monthly Electronics Spend and Monthly Household Spend']

    write_to_excel(titles, answers, 'Task 7')
