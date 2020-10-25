from service import write_to_excel, correl, numerical_key
import matplotlib.pyplot as plt


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

    # task 7.a
    x = list(df['Age'])
    y = list(df['Purchasing Frequency (every x months)'])
    plt.scatter(x, y)
    plt.title('Age and Purchasing Frequency')
    plt.show()

    #task 7.b
    x = list(df['Annual Income (x1000 $)'])
    y = list(df['TV Viewing (hours/day)'])
    plt.scatter(x, y)
    plt.axis([20, 70, 0, 15])
    plt.title('Annual Income and TV Viewing')
    plt.show()

    #task 7.d
    x = list(df['Monthly Household Spend'])
    y = list(df['Monthly Electronics Spend'])
    plt.scatter(x, y)
    plt.title('Monthly Electronics Spend and Monthly Household Spend')
    plt.show()
