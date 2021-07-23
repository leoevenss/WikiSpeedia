import pandas as pd

import csv

finpathsTSV='wikispeedia_paths-and-graph/wikispeedia_paths-and-graph/paths_finished.tsv'
finpathdf = pd.read_csv(finpathsTSV, sep='\t',skiprows=range(0,16),names=["hashedip","timestamp","durationinsec","path","rating"])

finpathlist=finpathdf['path'].values.tolist()

articleid = 'article-ids.csv'
article_ids = pd.read_csv(articleid,skiprows=[0,0],names=["article","articleId"])

articleidlist=article_ids['articleId'].values.tolist()

artid_dict=article_ids.set_index('article').T.to_dict('records')

artid_dict=artid_dict[0]

#artid_dict

artspdict=dict()#article shortest path dict

#articleidlist

fil="wikispeedia_paths-and-graph/wikispeedia_paths-and-graph/shortest-path-distance-matrix.txt"
with open(fil) as f:
        j=0
        lines = f.readlines()[17:]
        for line in lines:
            artspdict[articleidlist[j]]=line
            j+=1


with open('finished-paths-back.csv', mode='a',newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Human_Path_Length","Shortest_Path_Length","Ratio"])
    for i in finpathlist:
        path=i.split(";")
        humanlength=len(path)-1
        pathstart=path[0]
        pathend=path[humanlength]
        articlestartid=artid_dict[pathstart]
        articleendid=artid_dict[pathend]
        articleendid=int(articleendid[1:])
        shortestpath=artspdict[articlestartid][articleendid-1]
        if shortestpath == '_' :
            continue
        elif shortestpath == '0':
                continue
        else:
            ratio=(humanlength/int(shortestpath))
        csv_writer.writerow([humanlength,shortestpath,ratio])
            
        
    

with open('finished-paths-no-back.csv', mode='a',newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Human_Path_Length","Shortest_Path_Length","Ratio"])
    for i in finpathlist:
        path=i.split(";")
        
        stack = []
        for j in path:
            if j !='<':
                stack.append(i)
            elif j=='<':
                stack.pop()
        
        
        humanlength=(len(stack)-1)
        pathstart=path[0]
        pathend=path[len(path)-1]
        articlestartid=artid_dict[pathstart]
        articleendid=artid_dict[pathend]
        articleendid=int(articleendid[1:])
        shortestpath=artspdict[articlestartid][articleendid-1]
        if shortestpath == '_' :
            continue
        elif shortestpath == '0':
                continue
        else:
            ratio=(humanlength/int(shortestpath))
        
        
        csv_writer.writerow([humanlength,shortestpath,ratio])
    