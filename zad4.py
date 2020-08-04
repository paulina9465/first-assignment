import pandas as pd
import matplotlib.pyplot as pyplot

with open('survey_results_public.csv', 'rb') as data:
    df = pd.read_csv(data, usecols=['ConvertedComp', 'CodeRevHrs', 'BetterLife'])

    df.dropna(inplace=True)

    column_values1 = df[['ConvertedComp']].values.ravel()
    unique_values = pd.unique(column_values1)

    column_values2 = df[['CodeRevHrs']].values.ravel()
    unique_values2 = pd.unique(column_values2)
    df = df.astype({'ConvertedComp': 'int64', 'CodeRevHrs': 'int64'})

    #zad 5: Create chart for columns ConvertedComp, CodeRevHrs
    pyplot.plot(df['ConvertedComp'], df['CodeRevHrs'], 'ro', markersize=0.5)
    pyplot.xlabel('ConvertedComp')
    pyplot.ylabel('CodeRevHrs')
    pyplot.show()

    #Create chart for columns CodeRevHrs, ConvertedComp when values in BetterLife = Yes
    result = (df[(df['BetterLife'] == 'Yes')])
    pyplot.plot(result['ConvertedComp'], result['CodeRevHrs'], 'ro', markersize=0.5)
    pyplot.xlabel('ConvertedComp')
    pyplot.ylabel('CodeRevHrs')
    pyplot.show()

    ##Create chart for columns CodeRevHrs, ConvertedComp when values in BetterLife = No
    result2 = (df[(df['BetterLife'] == 'No')])
    pyplot.plot(result2['ConvertedComp'], result2['CodeRevHrs'], 'ro', markersize=0.5)
    pyplot.xlabel('ConvertedComp')
    pyplot.ylabel('CodeRevHrs')
    pyplot.show()