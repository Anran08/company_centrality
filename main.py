import networkx as nx
import pandas as pd
import os

input_directory='/Users/anrandu/Documents/Director Networks/data_by_year'
output_directory='/Users/anrandu/Documents/Director Networks/centrality_company'

input_file = input_directory + '/processed_subset_2018_matrix.csv'

'''
处理input file 输出到output_directory 中，跟sample.csv 一摸一样
'''

# 1. 用pandas导入csv文件

# 2. 用 df.values方法把df变成一个numpy 的 array

# 3.利用nx.from_numpy_array(array) 方法初始化graph

# 4. 分别调用对应方法nx.degree_centrality(G),nx.eigenvector_centrality_numpy(G), nx.closeness_centrality(G) 得到三个字典

# 5. 把

G = nx.read_edgelist

