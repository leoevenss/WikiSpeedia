import pandas as pd
import csv

finpathsTSV='wikispeedia_paths-and-graph/wikispeedia_paths-and-graph/paths_finished.tsv'
finpathdf = pd.read_csv(finpathsTSV, sep='\t',skiprows=range(0,16),names=["hashedip","timestamp","durationinsec","path","rating"])

finpathlist=finpathdf['path'].values.tolist()

articleids = {}
with open('article-ids.csv', 'r', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader) # toss headers
    for artid, artname in reader:
        articleids.setdefault(artid, []).append(artname)

#articleids

art_cat = {}
with open('article-categories.csv', 'r', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader) # toss headers
    for artid, artname in reader:
        #art[artid]=artname.split(",")
        art_cat[artid]=[x.strip() for x in artname.split(',')]

categoryTSV='wikispeedia_paths-and-graph/wikispeedia_paths-and-graph/categories.tsv'
categories_tsv = pd.read_csv(categoryTSV,skiprows=range(0,13),names=['article','category'], sep='\t')


art_catdict=dict()
for i in range(categories_tsv['article'].size):
    key=categories_tsv['article'][i]
    cat_val=categories_tsv['category'][i]
    if key not in art_catdict.keys():
        art_catdict[key]=set()
        art_catdict[key].add(cat_val)
    else:
        art_catdict[key].add(cat_val)
        

#art_catdict

newdict=dict()
for key,value in art_catdict.items():
    temp=set()
    for i in value:
        for j in range(i.count(".")+1):
            temp.add(i.rsplit(".",j)[0])
    newdict[key]=temp
            

#newdict

categoryids = {}
with open('category-ids.csv', 'r', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader) # toss headers
    for artid, artname in reader:
        categoryids.setdefault(artid, []).append(artname)

mapdict=dict()
for key,value in newdict.items():
    vallist=list()
    for v in value:
        vallist.append(categoryids[v][0])
    mapdict[key]=vallist

#mapdict

artcatd=dict()
for key,val in mapdict.items():
    artcatd[articleids[key][0]]=val







#artcatd['A3254']

#art_cat

articleidlist=list()
for key,value in articleids.items():
    articleidlist.append(value[0])

#articleidlist

for i in articleidlist:
    if i not in artcatd.keys():
        artcatd[i]=['C0001']

#len(artcatd)



artspdict=dict()
fil="wikispeedia_paths-and-graph/wikispeedia_paths-and-graph/shortest-path-distance-matrix.txt"
with open(fil) as f:
        j=0
        lines = f.readlines()[17:]
        for line in lines:
            artspdict[articleidlist[j]]=line
            j+=1

#artspdict

#finpathlist

pathhspdict=dict()
for i in finpathlist:
        path=i.split(";")
        if len(path)==1:
            continue
        if path[0]=='Bird' and path[-1]=='Wikipedia_Text_of_the_GNU_Free_Documentation_License':
            continue
    
        stack = []
        for j in path:
            if j !='<':
                stack.append(i)
            elif j=='<':
                stack.pop()
        
        #print(path)
        humanlength=(len(stack)-1)
        #print(humanlength)
        pathstart=path[0]
        #print(pathstart)
        pathend=path[len(path)-1]
        #print(pathend)
        articlestartid=articleids[pathstart][0]
        #print(articlestartid)
        articleendid=articleids[pathend][0]
        #print(articleendid)
        articleend=int(articleendid[1:])
        #print(articleendid)
        lis=list((x,y) for x in artcatd[articlestartid] for y in artcatd[articleendid])
        #print(lis)
        
        shortestpath=artspdict[articlestartid][articleend-1]
        for val in lis:
            if val in pathhspdict.keys():
                pathhspdict[val][0]=pathhspdict[val][0]+humanlength
                pathhspdict[val][1]=pathhspdict[val][1]+int(shortestpath)
                pathhspdict[val][2]=pathhspdict[val][2]+1
                
            else:
                pathhspdict[val]=[humanlength,int(shortestpath),1]
        #print(shortestpath)

#len(pathhspdict)



ratiodict=dict()
for key, value in pathhspdict.items():
    if value[1]!=0:
        ratiodict[key]=((value[0]/value[2])/(value[1]/value[2]))
    else:
        ratiodict[key]=0

from collections import OrderedDict 

dict1 = OrderedDict(sorted(ratiodict.items())) 

with open('category-ratios.csv', mode='a',newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["From_Category","To_Category","Ratio_of_human_to_shortest"])
    for key,value in dict1.items():
        csv_writer.writerow([key[0],key[1],value])

