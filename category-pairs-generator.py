import pandas as pd
import csv

articleids = {}
with open('article-ids.csv', 'r', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader) # toss headers
    for artid, artname in reader:
        articleids.setdefault(artid, []).append(artname)

art_cat = {}
with open('article-categories.csv', 'r', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader) # toss headers
    for artid, artname in reader:
        #art[artid]=artname.split(",")
        art_cat[artid]=[x.strip() for x in artname.split(',')]

categoryids = {}
with open('category-ids.csv', 'r', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader) # toss headers
    for artid, artname in reader:
        categoryids.setdefault(artid, []).append(artname)

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
        

articlelist=list(articleids.keys())

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
            



mapdict=dict()
for key,value in newdict.items():
    vallist=list()
    for v in value:
        vallist.append(categoryids[v][0])
    mapdict[key]=vallist



finpathsTSV='wikispeedia_paths-and-graph/wikispeedia_paths-and-graph/paths_finished.tsv'
finpathdf = pd.read_csv(finpathsTSV, sep='\t',skiprows=range(0,16),names=["hashedip","timestamp","durationinsec","path","rating"])
finpathlist=finpathdf['path'].values.tolist()

dictpair=dict()
#pathdictpair=dict()
count=0
for i in range(len(finpathlist)):
    st_art=finpathlist[i].split(";")[0]
    end_art=finpathlist[i].split(";")[-1]
    if len(finpathlist[i].split(";"))==1:
        continue
    if st_art=='Bird' and end_art=='Wikipedia_Text_of_the_GNU_Free_Documentation_License':
        continue
    
    lis=list((x,y) for x in mapdict[st_art] for y in mapdict[end_art])
    #print(lis)
    #pathdictpair[i]=lis
    #lis=set(tuple(sorted(row)) for row in lis)
    for val in lis:
        
        if tuple(val) not in dictpair.keys():
            count+=1
            dictpair[tuple(val)]=1
        else:
            dictpair[tuple(val)]=dictpair[tuple(val)]+1
    

unfinpathsTSV='wikispeedia_paths-and-graph/wikispeedia_paths-and-graph/paths_unfinished.tsv'
unfinpathdf = pd.read_csv(unfinpathsTSV, sep='\t',skiprows=range(0,17),names=["hashedip","timestamp","durationinsec","path","dest","rating"])
unfinpathsrc=unfinpathdf['path'].values.tolist()
unfinpathdest=unfinpathdf['dest'].values.tolist()

srcunfin=list()
for i in unfinpathsrc:
    srcunfin.append(i.split(";")[0])

#from fuzzywuzzy import process

#def getmatch(query,choice,limit=5):
#    result=process.extract(query,choice,limit=limit)
#    return result



#unmat=[]
#for dis in unmatched:
#    match=getmatch(dis,articlelist)
#    #print(dis,match)
      

spmist={
    
 'Black_ops_2':'',
 'C++':'',
 'Christmas':'',
 'Fats':'',
 'Great':'',
 'Kashmir':'',
 'Macedonia':'',
 'Mustard':'',
 'Netbook':'',
 'Rat':'',
 'Sportacus':'',
 'Test':'',
 'The':'',
 'The_Rock':'',
 'Usa':'',
 'Western_Australia':'',
'Long_peper':'Long_pepper',
'Rss':'RSS_%28file_format%29',
'Charlottes_web':'Charlotte%27s_Web', 
'Georgia':'Georgia_%28country%29',
'English':'English_language',
'_Zebra':'Zebra',
'Podcast':'Podcasting',
'Bogota': 'Bogot%C3%A1',
'Adolph_Hitler': 'Adolf_Hitler'
}

#unfidictpair=dict()
#for i in finpathlist:
#    st_art=i.split(";")[0]
#    end_art=i.split(";")[-1]
    
#    lis=list([x,y] for x in mapdict[st_art] for y in mapdict[end_art])
    
    #lis=set(tuple(sorted(row)) for row in lis)
#    for val in lis:
#        if tuple(val) not in dictpair.keys():
#            dictpair[tuple(val)]=1
#        else:
#            dictpair[tuple(val)]=dictpair[tuple(val)]+1
    

for key,value in spmist.items():
    if value == '':
        mapdict[key]=['C0001']

unfidictpair=dict()
for i in range(len(srcunfin)):
    unsrc=srcunfin[i]
    undest=unfinpathdest[i]
    if undest in spmist.keys():
        if spmist[undest]!='':
            undest=spmist[undest]
    unlis=list([x,y] for x in mapdict[unsrc] for y in mapdict[undest])
    for val in unlis:
        if tuple(val) not in unfidictpair.keys():
            unfidictpair[tuple(val)]=1
        else:
            unfidictpair[tuple(val)]=unfidictpair[tuple(val)]+1
    

catids=list()
for key,value in categoryids.items():
    catids.append(value[0])

totalpairs=list((x,y) for x in catids for y in catids)
    

totalpairs.sort()

with open('category-pairs.csv', mode='a',newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["From_Category","To_Category","Percentage_of_finished_paths","Percentage_of_unfinished_paths"])
    for pair in totalpairs:
        finpair=unfinpair=total=0
        if pair in dictpair.keys():
            finpair=dictpair[pair]
        if pair in unfidictpair.keys():
            unfinpair=unfidictpair[pair]
        total=finpair+unfinpair
        if total!=0:
            finperc=(finpair/total)*100
            unfinperc=(unfinpair/total)*100
        else:
            finperc=0
            unfinperc=0
        csv_writer.writerow([pair[0],pair[1],finperc,unfinperc])
    
    



#for key,value in unfidictpair.items():
#    if key not in dictpair.keys():
#        dictpair[key]=value

#len(dictpair)