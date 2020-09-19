import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
import seaborn as sns


#dependent variable (y):  WorkWeekHrs , independent variables (x1, x2): CompTotal, CodeRevHrs
#Choose 5 columns with numeric values, 1 column with text values and 1 column with qualitative data
df = pd.read_csv('survey_results_public.csv', usecols=['YearsCode', 'Age1stCode', 'CompTotal', 'WorkWeekHrs',
                       'CodeRevHrs', 'Hobbyist', 'MainBranch'])

df.dropna(inplace=True)
df.replace(to_replace={'Yes': '1', 'No': '0'}, inplace=True)
#Looking for dependencies between columns
print(df.corr())

# using one-hot encoding metod
one_hot = pd.get_dummies(df['MainBranch'])
df = df.drop('MainBranch',axis = 1)
df = df.join(one_hot)

#Calculate the arithmetic mean and standard deviation
mean1 = (np.mean(df['CompTotal']))
sd1 = np.std(df['CompTotal'])

mean2 = (np.mean(df['WorkWeekHrs']))
sd2 = np.std(df['WorkWeekHrs'])

#Remove outliers using standard deviation
result = df[(df['CompTotal'] >= (mean1 - 2 *sd1))]

#Remove outliers using standard deviation
result2 = result[(result['WorkWeekHrs'] >= (mean2 - 2 *sd2))]

#Remove outliers using standard quantile
kwantyl2 = result2[(result2['CodeRevHrs'] >= result2['CodeRevHrs'].quantile(.15)) & (result2['CodeRevHrs'] <=
            result2['CodeRevHrs'].quantile(.85))]


#Create charts
sns.boxplot(y=kwantyl2['WorkWeekHrs'], x=kwantyl2['CodeRevHrs'], data=kwantyl2)
plt.show()
sns.boxplot(y=kwantyl2['WorkWeekHrs'], x=kwantyl2['CodeRevHrs'], data=kwantyl2)
plt.show()

sns.regplot(y=kwantyl2['WorkWeekHrs'], x=kwantyl2['CompTotal'])
plt.show()

sns.jointplot(x=kwantyl2['CompTotal'], y=kwantyl2['WorkWeekHrs'], data=kwantyl2, kind='reg')
plt.show()

#Create linear regression model
rl = linear_model.LinearRegression()
rl.fit(kwantyl2[['CodeRevHrs']], kwantyl2[['WorkWeekHrs']])
print(rl.predict([[12]]))
print(rl.predict([[40]]))
mse = np.mean((rl.predict(kwantyl2[['CodeRevHrs']]) - kwantyl2[['WorkWeekHrs']]) ** 2)
print("Error:", mse)

rl = linear_model.LinearRegression()
rl.fit(kwantyl2[['CompTotal', 'CodeRevHrs']], kwantyl2[['WorkWeekHrs']])
print(rl.coef_)
mse = np.mean((rl.predict(kwantyl2[['CodeRevHrs', 'CompTotal']]) - kwantyl2[['WorkWeekHrs']]) ** 2)
print("Error:", mse)

rl = linear_model.LinearRegression()
rl.fit(kwantyl2[['CompTotal', 'CodeRevHrs', 'Hobbyist']], kwantyl2[['WorkWeekHrs']])
mse = np.mean((rl.predict(kwantyl2[['CodeRevHrs', 'CompTotal', 'Hobbyist']]) - kwantyl2[['WorkWeekHrs']]) ** 2)
print("Error:", mse)




