import pandas as pd
import numpy as np

with open('train.tsv', 'rb') as data:
    df = pd.read_csv(data, names=['A', 'B', 'C', 'D', 'E', 'F'], sep='\t')
 #calculate price per meter
    metr = df['A']/df['C']

    df['metr'] = metr
 #calculate mean for price per meter
    avgmetr = np.mean(df['metr'])
    print(avgmetr)
#select rows where there are more than two rooms and price is lower than mean price per meter
    conditions = (df[(df['B'] >=3) & (df['metr'] < avgmetr)])
 #save result to output file
    conditions.to_csv('out1.csv', columns=['B', 'A', 'metr'], header=False, sep='\t')