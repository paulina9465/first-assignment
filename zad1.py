import pandas as pd
import numpy as np

with open('train.tsv', 'rb') as data:
    df = pd.read_csv(data, names=['A', 'B', 'C', 'D', 'E', 'F'], sep='\t')
#calculate mean price
    avg = round(np.mean(df['A']), 0)
    print(avg)
 #open file and write mean 
    f = open('out0.csv ', "w")
    f.write(str(avg))