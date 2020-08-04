import pandas as pd
import numpy as np

with open('train.tsv', 'rb') as data:
    df = pd.read_csv(data, names=['A', 'B', 'C', 'D', 'E', 'F'], sep='\t')
    metr = df['A']/df['C']

    df['metr'] = metr

    avgmetr = np.mean(df['metr'])
    print(avgmetr)

    conditions = (df[(df['B'] >=3) & (df['metr'] < avgmetr)])
    conditions.to_csv('out1.csv', columns=['B', 'A', 'metr'], header=False, sep='\t')