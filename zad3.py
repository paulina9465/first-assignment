import pandas

trainFile = pandas.read_csv('train.tsv', names=['A', 'B', 'C', 'D', 'E', 'F'], sep='\t')
descriptionFile = pandas.read_csv('description.csv')

result = trainFile.join(descriptionFile.set_index('liczba'), on='D')
result.to_csv('out2.csv', header=False, sep='\t')