import pandas as pd
import numpy as np

with open('train.tsv', 'rb') as data:
    df = pd.read_csv(data, names=['A', 'B', 'C', 'D', 'E', 'F'], sep='\t')
    avg = round(np.mean(df['A']), 0)
    print(avg)
    f = open('out0.csv ', "w")
    f.write(str(avg))