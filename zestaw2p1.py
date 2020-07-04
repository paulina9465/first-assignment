import pandas
import numpy
from sklearn.preprocessing import OneHotEncoder
import sklearn
import matplotlib.pyplot
import matplotlib.pyplot
import seaborn
import numpy
from sklearn import linear_model
from scipy import stats

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
result2 = file[(file['WorkWeekHrs'] >= (mean2 - 2 *sd2))]
print(result2)
result3 = file[(file['CodeRevHrs'] >= (mean3 - 2 *sd3))]
print(result3)


kwantyl1 = file[(file['CompTotal'] >= file['CompTotal'].quantile(.15)) & (file['CompTotal'] <=
        file['CompTotal'].quantile(.85))]
print(kwantyl1)

kwantyl2 = file[(file['WorkWeekHrs'] >= file['WorkWeekHrs'].quantile(.15)) & (file['WorkWeekHrs'] <=
        file['WorkWeekHrs'].quantile(.85))]
print(kwantyl2)

kwantyl2 = file[(file['CodeRevHrs'] >= file['CodeRevHrs'].quantile(.15)) & (file['CodeRevHrs'] <=
        file['CodeRevHrs'].quantile(.85))]
print(kwantyl2)

