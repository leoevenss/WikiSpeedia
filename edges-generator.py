import pandas as pd
import csv

articleid = 'article-ids.csv'
article_ids = pd.read_csv(articleid,skiprows=[0,0],names=["article","articleId"])

articleidlist=article_ids['articleId'].values.tolist()

fil="wikispeedia_paths-and-graph/wikispeedia_paths-and-graph/shortest-path-distance-matrix.txt"

with open('edges.csv', mode='a',newline='') as csv_file:
    
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["From_ArticleID","To_ArticleID"])
    with open(fil) as f:
        j=0
        lines = f.readlines()[17:]
        for line in lines:
            
            row=line
            for i in range(len(row)-1):
                if row[i]!='1':
                    continue
                else:
                        #print(articleidlist[0],":",articleidlist[i])
                    csv_writer.writerow([articleidlist[j],articleidlist[i]])
            j+=1
            i=0
        f.close()             