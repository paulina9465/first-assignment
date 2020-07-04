import pandas
import matplotlib.pyplot
import matplotlib.pyplot
import seaborn
import numpy
from sklearn import linear_model
from scipy import stats

#zmienna zależna (y):  WorkWeekHrs , niezalezne zmienne (x1, x2): CompTotal, CodeRevHrs
file = pandas.read_csv('survey_results_public.csv', usecols=['YearsCode', 'Age1stCode', 'CompTotal', 'WorkWeekHrs',
                       'CodeRevHrs'])

file.dropna(inplace=True)

print(file.corr())
print(file.describe())