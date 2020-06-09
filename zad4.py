import pandas
import matplotlib.pyplot as pyplot

file = pandas.read_csv('survey_results_public.csv', usecols=['ConvertedComp', 'CodeRevHrs', 'BetterLife'])
print(file)

file.dropna(inplace=True)
print(file)

column_values1 = file[['ConvertedComp']].values.ravel()
unique_values = pandas.unique(column_values1)

column_values2 = file[['CodeRevHrs']].values.ravel()
unique_values2 = pandas.unique(column_values2)
file = file.astype({'ConvertedComp': 'int64', 'CodeRevHrs': 'int64'})

pyplot.plot(file['ConvertedComp'], file['CodeRevHrs'], 'ro', markersize=0.5)
pyplot.xlabel('ConvertedComp')
pyplot.ylabel('CodeRevHrs')
pyplot.show()

result = (file[(file['BetterLife'] == 'Yes')])
pyplot.plot(result['ConvertedComp'], result['CodeRevHrs'], 'ro', markersize=0.5)
pyplot.xlabel('ConvertedComp')
pyplot.ylabel('CodeRevHrs')
pyplot.show()

result2 = (file[(file['BetterLife'] == 'No')])
pyplot.plot(result2['ConvertedComp'], result2['CodeRevHrs'], 'ro', markersize=0.5)
pyplot.xlabel('ConvertedComp')
pyplot.ylabel('CodeRevHrs')
pyplot.show()