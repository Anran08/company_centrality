import networkx as nx
import pandas as pd
import numpy as np
import os

input_directory='/Users/anrandu/Documents/Director Networks/data_by_year'
output_directory='/Users/anrandu/Documents/Director Networks/centrality_company'

input_file = input_directory + "/" + 'processed_subset_2018_matrix.csv'

df = pd.read_csv(input_file, index_col=0)
matrix = df.values

print(matrix.shape)

G = nx.from_numpy_array(matrix)
mapping = {old_label: new_label for old_label, new_label in enumerate(df.index)}

# Relabel the nodes in the graph with the DataFrame index
G = nx.relabel_nodes(G, mapping)
#List of nodes with degree 0
isolated = [node for node, degree in dict(G.degree()).items() if degree == 0]

# Remove nodes with degree 0
G.remove_nodes_from(isolated)
print(G)

node_degree_dict = dict(G.degree())

# Print out the nodes and their corresponding degrees
for node, degree in node_degree_dict.items():
    print(f"Node {node} has degree {degree}")

degree_centrality = nx.degree_centrality(G)

# Calculate Eigenvector Centrality
eigenvector_centrality = nx.eigenvector_centrality(G,max_iter=100)

# Calculate Closeness Centrality
closeness_centrality = nx.closeness_centrality(G)

degree_df = pd.DataFrame.from_dict(degree_centrality, orient='index', columns=['degree_centrality'])
eigenvector_df = pd.DataFrame.from_dict(eigenvector_centrality, orient='index', columns=['eigenvector_centrality'])
closeness_df = pd.DataFrame.from_dict(closeness_centrality, orient='index', columns=['closeness_centrality'])
print(eigenvector_df)

# centralities_df = degree_df.join([eigenvector_df, closeness_df])
#
# centralities_df.to_csv(output_directory+'/test.csv',index=True)