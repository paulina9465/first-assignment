import pandas
import numpy

file = pandas.read_csv('train.tsv', names=['A', 'B', 'C', 'D', 'E', 'F'], sep='\t')
metr = file['A']/file['C']

file['metr'] = metr

avgmetr = numpy.mean(file['metr'])
print(avgmetr)

conditions = (file[(file['B'] >=3) & (file['metr'] < avgmetr)])
conditions.to_csv('out1.csv', columns=['B', 'A', 'metr'], header=False, sep='\t')