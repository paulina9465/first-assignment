import pandas
import numpy

file = pandas.read_csv('train.tsv', names=['A', 'B', 'C', 'D', 'E', 'F'], sep='\t')
avg = round(numpy.mean(file['A']), 0)
print(avg)
f = open('out0.csv ', "w")
f.write(str(avg))