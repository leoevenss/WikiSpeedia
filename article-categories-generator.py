import pandas as pd
import csv

categoryTSV='wikispeedia_paths-and-graph/wikispeedia_paths-and-graph/categories.tsv'
categories_tsv = pd.read_csv(categoryTSV,skiprows=range(0,13),names=['article','category'], sep='\t')

articleid = 'article-ids.csv'
article_ids = pd.read_csv(articleid,skiprows=[0,0],names=["article","articleId"])

categoryid = 'category-ids.csv'
category_ids = pd.read_csv(categoryid,skiprows=[0,0],names=["category","categoryid"])

art_catdict=dict()

for i in range(categories_tsv['article'].size):
    key=categories_tsv['article'][i]
    #cat_val=categories_tsv['category'][i].split(".")
    cat_val=categories_tsv['category'][i]
    if key not in art_catdict.keys():
        art_catdict[key]=set()
        #for j in range(len(cat_val)):
        #art_catdict[key].add('.'.join(cat_val[:j+1]))
        art_catdict[key].add(cat_val)
    else:
        art_catdict[key].add(cat_val)
        #for j in range(len(cat_val)):
            #art_catdict[key].add('.'.join(cat_val[:j+1]))

catid_dict=category_ids.set_index('category').T.to_dict('records')


catid_dict=catid_dict[0]

artid_dict=article_ids.set_index('article').T.to_dict('records')


artid_dict=artid_dict[0]

article_categdict=dict()
for key,v in artid_dict.items():
    if key in art_catdict.keys():
        article_categdict[artid_dict[key]]=list()
        for i in art_catdict[key]:
            if i in  catid_dict.keys():
                article_categdict[artid_dict[key]].append(catid_dict[i])
    else:
        article_categdict[artid_dict[key]]=list()
        article_categdict[artid_dict[key]].append('C0001')

with open('article-categories.csv', mode='a',newline='') as csv_file:
    
        csv_writer = csv.writer(csv_file,delimiter=',')
        csv_writer.writerow(["Article_ID","Category_ID"])
        
        for key,value in article_categdict.items():
                value.sort()
                val=(','.join(value))
                csv_writer.writerow([key,val])
