import pandas as pd
import networkx as nx
import csv

G=nx.DiGraph()

d = {}
with open('article-ids.csv', 'r', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader) # toss headers
    for artname, artid in reader:
        d.setdefault(artname, []).append(artid)

art = {}
with open('article-categories.csv', 'r', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader) # toss headers
    for artid, artname in reader:
        #art[artid]=artname.split(",")
        art[artid]=[x.strip() for x in artname.split(',')]

with open('edges.csv', newline='') as f:
    reader = csv.reader(f,delimiter=',')
    next(f)
    data = list(reader)



for i in data:
    G.add_edge(i[0],i[1])

finpathsTSV='wikispeedia_paths-and-graph/wikispeedia_paths-and-graph/paths_finished.tsv'
finpathdf = pd.read_csv(finpathsTSV, sep='\t',skiprows=range(0,16),names=["hashedip","timestamp","durationinsec","path","rating"])
finpathlist=finpathdf['path'].values.tolist()

splist=list()
count=1
for i in finpathlist:
    st_art=i.split(";")[0]
    end_art=i.split(";")[-1]
    count+=1
    if st_art=='Bird' and end_art=='Wikipedia_Text_of_the_GNU_Free_Documentation_License':
        continue
    if len(i.split(";"))==1:
        continue
    splist.append(nx.shortest_path(G,d[st_art][0],d[end_art][0]))

spcatpathdict=dict()
spcattimesdict=dict()
for i in range(len(splist)):
    sls=list()
    for j in splist[i]:
        #print(j)
        for s in art[j]:
            sls.append(s)
    for k in sls:
        if k not in spcattimesdict.keys():
            spcattimesdict[k]=1
        else:
            spcattimesdict[k]=spcattimesdict[k]+1
    mls=set(sls)
    for z in mls:
        if z not in spcatpathdict.keys():
            spcatpathdict[z]=1
        else:
            spcatpathdict[z]=spcatpathdict[z]+1
            
            #if s not in spcattimesdict.keys():
            #    spcattimesdict[s]=1
            #else:
            #    spcattimesdict[s]=spcattimesdict[s]+1
            

hpcatpathdict=dict()
hpcattimesdict=dict()
count=0
for path in finpathlist:
    artlist=path.split(";")
    if artlist[0]=='Bird' and artlist[-1]=='Wikipedia_Text_of_the_GNU_Free_Documentation_License':
        
        continue
    if len(path.split(";"))==1:
        #print(path)
        continue
    #to remove backlinks
    #count+=1
    #i=0
    #artlist
    if len(artlist)>1:
        i=0
        while(i<len(artlist)-1):
            if artlist[i+1]=='<':
                artlist.pop(i)
                artlist.pop(i)
                if artlist[i]=='<':
                    i-=1
            else:
                    i+=1
    
    

    catlist=list()
    ls=set()
    for k in artlist:
    
        
        artid=d[k]
        for val in art[artid[0]]:
            catlist.append(val)
    for b in catlist:
        #print(b)
        if b not in hpcattimesdict.keys():
            hpcattimesdict[b]=1
        else:
            hpcattimesdict[b]=hpcattimesdict[b]+1
    ls=set(catlist)
    #print(ls)
    for c in ls:
        #print(c)
        if c not in hpcatpathdict.keys():
            hpcatpathdict[c]=1
        else:
            hpcatpathdict[c]=hpcatpathdict[c]+1
    
    

catidslist = []
with open('category-ids.csv', 'r', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader) # toss headers
    for catname, catid in reader:
        catidslist.append(catid)
        #d.setdefault(artname, []).append(artid)

catidslist.sort()

with open('category-paths.csv', mode='a',newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Category_ID","Number_of_human_paths_traversed","Number_of_human_times_traversed","Number_of_shortest_paths_traversed","Number_of_shortest_times_traversed"])
    for i in catidslist:
        if i in spcatpathdict.keys():
            csv_writer.writerow([i,hpcatpathdict[i],hpcattimesdict[i],spcatpathdict[i],spcattimesdict[i]])
        else:
            csv_writer.writerow([i,0,0,0,0])
    
