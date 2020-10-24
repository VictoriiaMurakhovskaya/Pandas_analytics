from service import write_to_excel


def runtask(df, window):
    # task4a
    y = df.loc[(df['Gender'] == 'male') & (df['Marital Status'] == 'married') & (df['Technology Adoption'] == 'early')]
    y['key value'] = y['Monthly Electronics Spend'] * 24 - 499
    y = y.loc[y['key value'] > 0]
    answers = [y.shape[0]]

    #task4b
    y = df.loc[(df['Gender'] == 'female') & (df['Education'].isin(['MA', 'PhD'])) &
               (df['Purchasing Decision-maker'] == 'single')]
    answers.append(y.shape[0])

    #task4c
    y = df.loc[(df['Technology Adoption'] == 'early') & (df['Purchasing Location'] == 'specialty stores') &
               (df['Purchasing Frequency (every x months)'] < 13)]
    answers.append(y.shape[0])

    #task4d
    y = df.loc[(df['Age'] > 65) & (df['TV Viewing (hours/day)'] > 6)]
    answers.append(y.shape[0])
    answers.append(min(list(y['Annual Income (x1000 $)'])))
    answers.append(max(list(y['Annual Income (x1000 $)'])))
    answers.append(y['Annual Income (x1000 $)'].mean())

    titles = ['Task 4.a', 'Task 4.b', 'Task 4.c', 'Task 4.d', 'Task 4.d (min income)', 'Task 4.d (max income)',
              'Task 4.d (avg income)']

    write_to_excel(titles, answers, 'Task 4')



