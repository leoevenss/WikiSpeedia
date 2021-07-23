import pandas as pd
import networkx as nx
import csv

G = nx.Graph()


with open('edges.csv', newline='') as f:
    reader = csv.reader(f,delimiter=',')
    next(f)
    data = list(reader)



edgesids = pd.read_csv('edges.csv',skiprows=[0,0],names=["edge1","edge2"])

articleids = pd.read_csv('article-ids.csv',skiprows=[0,0],names=["artname","artid"])

articleids=articleids["artid"].values.tolist()

a=set(edgesids['edge1'].values.tolist())

b=set(edgesids['edge2'].values.tolist())

a=a|b

s=list()
for i in articleids:
        if i not in a:
            s.append(i)
            


for i in range(len(data)):
    G.add_nodes_from([data[i][0],data[i][1]])
    G.add_edge(data[i][0],data[i][1])

for j in s:
    G.add_node(j)

components  = list(G.subgraph(c).copy() for c in sorted(nx.connected_components(G), key=len, reverse=False))

with open('graph-components.csv', mode='a',newline='') as csv_file:
    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Nodes","Edges","Diameter"])
        for i in range(len(components)):            
                csv_writer.writerow([len(components[i].nodes),len(components[i].edges),nx.diameter(components[i])])
