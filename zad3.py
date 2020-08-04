import pandas as pd

with open('train.tsv', 'rb') as data, open('description.csv') as data2:
    df = pd.read_csv(data, names=['A', 'B', 'C', 'D', 'E', 'F'], sep='\t')
    df2 = pd.read_csv(data2)

    result = df.join(df2.set_index('liczba'), on='D')
    result.to_csv('out2.csv', header=False, sep='\t')