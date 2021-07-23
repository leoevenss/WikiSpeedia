import pandas as pd
import csv
from collections import OrderedDict 
from queue import Queue 

categoryTSV='wikispeedia_paths-and-graph/wikispeedia_paths-and-graph/categories.tsv'

categories_read = pd.read_csv(categoryTSV,skiprows=range(0,13),names=['article','category'], sep='\t')

catlist=list()

catdict=dict()

totalsize=categories_read['category'].size
for j in range(totalsize):
    catlist=categories_read['category'][j].split(".")
    for i in range(len(catlist)-1):
        parent='.'.join(catlist[:i+1])
        child='.'.join(catlist[:i+2])

        if parent not in catdict.keys():
            catdict[parent]=set()
            catdict[parent].add(child)

        else:

            catdict[parent].add(child)

        

for key,value in catdict.items():
    catdict[key]=sorted(value)

q=Queue()

catvaldict=dict()

val=1
parent='subject'
catvaldict[parent]='C000'+str(val)
for i in catdict['subject']:
    q.put(i)
while 1:
    if (q.empty()==False):
        #val+=1
        parent=q.get()
        if parent not in  catvaldict.keys():#see if this works
            val+=1
            if val<=9:
                catvaldict[parent]='C000'+str(val)
            elif val>=10 and val<=99:
                catvaldict[parent]='C00'+str(val)
            elif val>=100 and val<=200:
                catvaldict[parent]='C0'+str(val)
        if parent in catdict.keys():
            for j in  catdict[parent]:
                if j not in catvaldict.keys() :
                    q.put(j)
    else:
        break


sortedcatdict = OrderedDict(sorted(catvaldict.items())) 


with open('category-ids.csv', mode='a',newline='') as csv_file:
    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Category_Name","Category_ID"])

        for key,value in sortedcatdict.items():            
                csv_writer.writerow([key,value])
