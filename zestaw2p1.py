import pandas
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