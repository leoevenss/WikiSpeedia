import pandas as pd
import csv

articleTSV = 'wikispeedia_paths-and-graph/wikispeedia_paths-and-graph/articles.tsv'

with open(articleTSV, newline='') as f:
    reader = csv.reader(f)
    articles = list(reader)
f.close()

articlelist=articles[12:]


value=list()
i=1
while i <= len(articlelist):
    if(i<=9):
        value.append('A000'+str(i))
    elif (i>=10 and i<=99):
        value.append('A00'+str(i))
    elif(i>=100 and i<=999):
        value.append('A0'+str(i))
    elif(i>=1000):
        value.append('A'+str(i))
    i+=1

i=1
with open('article-ids.csv', mode='a',newline='') as csv_file:
    
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Article_Name","Article_ID"])
        for i in range(len(value)):            
                csv_writer.writerow([articlelist[i][0],value[i]])
        