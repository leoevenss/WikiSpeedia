import pandas as pd
from urllib.parse import unquote
import csv

fpwb=pd.read_csv("finished-paths-back.csv")




#path=fpwb["path"].values.tolist()
humanlength=fpwb["Human_Path_Length"].values.tolist()
shortestpath=fpwb["Shortest_Path_Length"].values.tolist()

lenpath=len(humanlength)

hpsame=hp1=hp2=hp3=hp4=hp5=hp6=hp7=hp8=hp9=hp10=hp11nm=0
for i in range(len(humanlength)):
    if (humanlength[i]-shortestpath[i])==0:
        hpsame+=1
    elif (humanlength[i]-shortestpath[i])==1:
        hp1+=1
    elif (humanlength[i]-shortestpath[i])==2:
        hp2+=1
    elif (humanlength[i]-shortestpath[i])==3:
        hp3+=1
    elif (humanlength[i]-shortestpath[i])==4:
        hp4+=1
    elif (humanlength[i]-shortestpath[i])==5:
        hp5+=1
    elif (humanlength[i]-shortestpath[i])==6:
        hp6+=1
    elif (humanlength[i]-shortestpath[i])==7:
        hp7+=1
    elif (humanlength[i]-shortestpath[i])==8:
        hp8+=1
    elif (humanlength[i]-shortestpath[i])==9:
        hp9+=1
    elif (humanlength[i]-shortestpath[i])==10:
        hp10+=1
    elif (humanlength[i]-shortestpath[i])>=11:
        hp11nm+=1
    
    

samepct=(hpsame/lenpath)*100
hp1pct=(hp1/lenpath)*100
hp2pct=(hp2/lenpath)*100
hp3pct=(hp3/lenpath)*100
hp4pct=(hp4/lenpath)*100
hp5pct=(hp5/lenpath)*100
hp6pct=(hp6/lenpath)*100
hp7pct=(hp7/lenpath)*100
hp8pct=(hp8/lenpath)*100
hp9pct=(hp9/lenpath)*100
hp10pct=(hp10/lenpath)*100
hp11nmpct=(hp11nm/lenpath)*100

with open('percentage-paths-back.csv', mode='a',newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Equal_Length","Larger_by_1","Larger_by_2","Larger_by_3","Larger_by_4","Larger_by_5","Larger_by_6","Larger_by_7","Larger_by_8","Larger_by_9","Larger_by_10","Larger_by_more_than_10"])
    csv_writer.writerow([samepct,hp1pct,hp2pct,hp3pct,hp4pct,hp5pct,hp6pct,hp7pct,hp8pct,hp9pct,hp10pct,hp11nmpct])
    






#for no back edges

fpnb=pd.read_csv("finished-paths-no-back.csv")


#pathno=fpnb["path"].values.tolist()
humanlengthno=fpnb["Human_Path_Length"].values.tolist()
shortestpathno=fpnb["Shortest_Path_Length"].values.tolist()

lenpathno=len(humanlengthno)

hpsameno=hp1no=hp2no=hp3no=hp4no=hp5no=hp6no=hp7no=hp8no=hp9no=hp10no=hp11nmno=0
#wtf=0
#damnpa=list()

for i in range(len(humanlengthno)):
    if (humanlengthno[i]-shortestpathno[i])==0:
        hpsameno+=1
    elif (humanlengthno[i]-shortestpathno[i])==1:
        hp1no+=1
    elif (humanlengthno[i]-shortestpathno[i])==2:
        hp2no+=1
    elif (humanlengthno[i]-shortestpathno[i])==3:
        hp3no+=1
    elif (humanlengthno[i]-shortestpathno[i])==4:
        hp4no+=1
    elif (humanlengthno[i]-shortestpathno[i])==5:
        hp5no+=1
    elif (humanlengthno[i]-shortestpathno[i])==6:
        hp6no+=1
    elif (humanlengthno[i]-shortestpathno[i])==7:
        hp7no+=1
    elif (humanlengthno[i]-shortestpathno[i])==8:
        hp8no+=1
    elif (humanlengthno[i]-shortestpathno[i])==9:
        hp9no+=1
    elif (humanlengthno[i]-shortestpathno[i])==10:
        hp10no+=1
    elif (humanlengthno[i]-shortestpathno[i])>=11:
        hp11nmno+=1
    #elif (humanlengthno[i]-shortestpathno[i])<0:
        #damnpa.append(pathno[i]+str(i))
        #wtf+=1
    
    





samenopct=(hpsameno/lenpathno)*100
hp1nopct=(hp1no/lenpathno)*100
hp2nopct=(hp2no/lenpathno)*100
hp3nopct=(hp3no/lenpathno)*100
hp4nopct=(hp4no/lenpathno)*100
hp5nopct=(hp5no/lenpathno)*100
hp6nopct=(hp6no/lenpathno)*100
hp7nopct=(hp7no/lenpathno)*100
hp8nopct=(hp8no/lenpathno)*100
hp9nopct=(hp9no/lenpathno)*100
hp10nopct=(hp10no/lenpathno)*100
hp11nmnopct=(hp11nmno/lenpathno)*100





with open('percentage-paths-no-back.csv', mode='a',newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Equal_Length","Larger_by_1","Larger_by_2","Larger_by_3","Larger_by_4","Larger_by_5","Larger_by_6","Larger_by_7","Larger_by_8","Larger_by_9","Larger_by_10","Larger_by_more_than_10"])
    csv_writer.writerow([samenopct,hp1nopct,hp2nopct,hp3nopct,hp4nopct,hp5nopct,hp6nopct,hp7nopct,hp8nopct,hp9nopct,hp10nopct,hp11nmnopct])
    


