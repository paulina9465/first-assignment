import pandas
import numpy
from sklearn import linear_model


#zmienna zależna (y):  WorkWeekHrs , niezalezne zmienne (x1, x2): CompTotal, CodeRevHrs
file = pandas.read_csv('survey_results_public.csv', usecols=['YearsCode', 'Age1stCode', 'CompTotal', 'WorkWeekHrs',
                       'CodeRevHrs', 'Hobbyist', 'MainBranch'])

file.dropna(inplace=True)
file.replace(to_replace={'Yes': '1', 'No': '0'}, inplace=True)
print(file)
print(file.corr())

one_hot = pandas.get_dummies(file['MainBranch'])
file = file.drop('MainBranch',axis = 1)
file = file.join(one_hot)
print(file)

mean1 = (numpy.mean(file['CompTotal']))
print(mean1)
print('*****************************')
sd1 = numpy.std(file['CompTotal'])
print(sd1)

mean2 = (numpy.mean(file['WorkWeekHrs']))
print(mean2)
print('*****************************')
sd2 = numpy.std(file['WorkWeekHrs'])
print(sd2)

mean3 = (numpy.mean(file['CodeRevHrs']))
print(mean3)
print('*****************************')
sd3 = numpy.std(file['CodeRevHrs'])
print(sd3)

result = file[(file['CompTotal'] >= (mean1 - 2 *sd1))]
print(result)
result2 = result[(result['WorkWeekHrs'] >= (mean2 - 2 *sd2))]
print(result2)
kwantyl2 = result2[(result2['CodeRevHrs'] >= result2['CodeRevHrs'].quantile(.15)) & (result2['CodeRevHrs'] <=
            result2['CodeRevHrs'].quantile(.85))]
print(kwantyl2)

rl = linear_model.LinearRegression()
rl.fit(kwantyl2[['CodeRevHrs']], kwantyl2[['WorkWeekHrs']])
print(rl.predict([[12]]))
print(rl.predict([[40]]))
mse = numpy.mean((rl.predict(kwantyl2[['CodeRevHrs']]) - kwantyl2[['WorkWeekHrs']]) ** 2)
print("Error:", mse)


rl = linear_model.LinearRegression()
rl.fit(kwantyl2[['CompTotal', 'CodeRevHrs']], kwantyl2[['WorkWeekHrs']])
print(rl.coef_)
mse = numpy.mean((rl.predict(kwantyl2[['CodeRevHrs', 'CompTotal']]) - kwantyl2[['WorkWeekHrs']]) ** 2)
print("Error:", mse)

rl = linear_model.LinearRegression()
rl.fit(kwantyl2[['CompTotal', 'CodeRevHrs', 'Hobbyist']], kwantyl2[['WorkWeekHrs']])
mse = numpy.mean((rl.predict(kwantyl2[['CodeRevHrs', 'CompTotal', 'Hobbyist']]) - kwantyl2[['WorkWeekHrs']]) ** 2)
print("Error:", mse)




