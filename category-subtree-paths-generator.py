import pandas as pd
import csv

categoryTSV='wikispeedia_paths-and-graph/wikispeedia_paths-and-graph/categories.tsv'
#categories_tsv = pd.read_csv(categoryTSV, sep='\t')
categories_tsv = pd.read_csv(categoryTSV,skiprows=range(0,13),names=['article','category'], sep='\t')

articleid = 'article-ids.csv'
article_ids = pd.read_csv(articleid,skiprows=[0,0],names=["article","articleId"])


#categoryid = 'category-ids.csv'
#category_ids = pd.read_csv(categoryid,names=["category","categoryid"])


art_catdict=dict()
for i in range(categories_tsv['article'].size):
    key=categories_tsv['article'][i]
    cat_val=categories_tsv['category'][i]
    if key not in art_catdict.keys():
        art_catdict[key]=set()
        art_catdict[key].add(cat_val)
    else:
        art_catdict[key].add(cat_val)
        

articlelist=article_ids['article'].values.tolist()

for i in articlelist:
    if i not in art_catdict.keys():
        art_catdict[i]=set()
        art_catdict[i].add('subject')

newdict=dict()
for key,value in art_catdict.items():
    temp=set()
    for i in value:
        for j in range(i.count(".")+1):
            temp.add(i.rsplit(".",j)[0])
    newdict[key]=temp
            

categories = {}
with open('category-ids.csv', 'r', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader) # toss headers
    for artid, artname in reader:
        categories.setdefault(artid, []).append(artname)

finpathsTSV='wikispeedia_paths-and-graph/wikispeedia_paths-and-graph/paths_finished.tsv'
finpathdf = pd.read_csv(finpathsTSV, sep='\t',skiprows=range(0,16),names=["hashedip","timestamp","durationinsec","path","rating"])

finpathlist=finpathdf['path'].values.tolist()

import networkx as nx


G=nx.DiGraph()

with open('edges.csv', newline='') as f:
    reader = csv.reader(f,delimiter=',')
    data = list(reader)


art_dict = {}
with open('article-ids.csv', 'r', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader) # toss headers
    for artid, artname in reader:
        art_dict.setdefault(artid, []).append(artname)

edgelist=list()
for i in data:
    G.add_edge(i[0],i[1])

splist=list()
for i in finpathlist:
    st_art=i.split(";")[0]
    end_art=i.split(";")[-1]
    
    if st_art=='Bird' and end_art=='Wikipedia_Text_of_the_GNU_Free_Documentation_License':
        continue
    if len(i.split(";"))==1:
        continue
    splist.append(nx.shortest_path(G,art_dict[st_art][0],art_dict[end_art][0]))

mapdict=dict()
for key, value in newdict.items():
    uniqueset=set()
    for v in value:
        uniqueset.add(categories[v][0])
    mapdict[art_dict[key][0]]=uniqueset



spcatpathdict=dict()
spcattimesdict=dict()
for i in range(len(splist)):
    sls=list()
    for j in splist[i]:
        #print(j)
        for s in mapdict[j]:
            sls.append(s)
    for k in sls:
        if k not in spcattimesdict.keys():
            spcattimesdict[k]=1
        else:
            spcattimesdict[k]=spcattimesdict[k]+1
    #ls=set(sls)
    for z in set(sls):
        if z not in spcatpathdict.keys():
            spcatpathdict[z]=1
        else:
            spcatpathdict[z]=spcatpathdict[z]+1
            
            #if s not in spcattimesdict.keys():
            #    spcattimesdict[s]=1
            #else:
            #    spcattimesdict[s]=spcattimesdict[s]+1
            

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

#finpathlist=['14th_century;Europe;Republic_of_Ireland;<;<;Europe;<;Europe;Republic_of_Ireland;<;<;Time;Physics;Speed_of_light;Rainbow']
hpcatpathdict=dict()
hpcattimesdict=dict()
for path in finpathlist:
    artlist=path.split(";")
    if artlist[0]=='Bird' and artlist[-1]=='Wikipedia_Text_of_the_GNU_Free_Documentation_License':
        continue
    if len(path.split(";"))==1:
        #print(path)
        continue
    
    #to remove backlinks
    i=0
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
    for i in artlist:
        artid=d[i]
        #print(artid[0])
        for val in mapdict[artid[0]]:
            #for jk in val:
            catlist.append(val)
    #print(catlist)    
    for b in catlist:
        #print(b)
        if b not in hpcattimesdict.keys():
            hpcattimesdict[b]=1
        else:
            hpcattimesdict[b]=hpcattimesdict[b]+1
    #ls=set(sls)
    for c in set(catlist):
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

with open('category-subtree-paths.csv', mode='a',newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Category_ID","Number_of_human_paths_traversed","Number_of_human_times_traversed","Number_of_shortest_paths_traversed","Number_of_shortest_times_traversed"])
    for i in catidslist:
        if i in spcatpathdict.keys():
            csv_writer.writerow([i,hpcatpathdict[i],hpcattimesdict[i],spcatpathdict[i],spcattimesdict[i]])
        else:
            csv_writer.writerow([i,0,0,0,0])
    
