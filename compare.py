import pandas as pd
import os
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
directory='/Users/anrandu/Documents/Director Networks/centrality_company'
file1 = directory + '/sample_2018.csv'
file2 = directory + '/test.csv'

df1 = pd.read_csv(file1,index_col=0)
df2= pd.read_csv(file2,index_col=0)
df1 = df1.join(df2)
df1['divider'] = df1['eigencentrality'] / df1['eigenvector_centrality']

print(df1)

df1.to_csv(directory+'/compare.csv',index=True)