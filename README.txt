####Assignment2#######

PreReq:
python 3.8.2

1)pip3 install networkx

##################################
!!execute assign2.sh to execute all the programs ((Time Taken for entire Execution::3-4mins approximately))!!
!!Report is found inside the Report folder!!

################################################
Q1) execute article-ids-generator.sh : Output: article-ids.csv

Q2) execute category-ids-generator.sh : Output: category-ids.csv

Q3) execute article-categories-generator.sh : Output: article-categories.csv

###the below articles are assigned the category C0001###
['Directdebit', 'A1211']
['Donation', 'A1232']
['Friend_Directdebit', 'A1601']
['Pikachu', 'A3254']
['Sponsorship_Directdebit', 'A3850']
['Wowpurchase', 'A4546']


Q4) execute edges-generator.sh : Output: edges.csv

Q5) execute graph-components-generator.sh : Output: graph-components.csv
[The Graph is Considered to be Undirected]
[Used the networkx library to find the components, nodes , edges and diameter]


Q6) execute paths-finished-generator.sh : Output: finished-paths-back.csv;finished-paths-no-back.csv
[The Output is not sorted by 1st field as said by sir]

###the following 12 paths are ignored in question6 and in subsequent questions because the shortest path is '_' or '0' 
['Bird', 'Wikipedia_Text_of_the_GNU_Free_Documentation_License']
['Lesotho']
['Moon']
['Coal']
['Pyramid']
['Apple']
['Snow_Goose']
['Royal_Navy']
['Abel_Tasman']
['American_Samoa']
['Florence_Nightingale']
['William_and_Mary']


Q7) execute percentage-generator.sh : Output: percentage-paths-back.csv;percentage-paths-no-back.csv



Q8) execute category-paths-generator.sh : Output: category-paths.csv


Q9) execute category-subtree-paths-generator.sh : Output: category-subtree-paths.csv
[if there are two categories for a single article ; the parents are considered only once ; for example if parents of two categories of article are subject , then count subject once]


Q10) execute category-pairs-generator.sh : Output: category-pairs.csv
###the following articles(the destination/target - unfinished-paths.tsv) are either having spelling mistakes or not found in article list  
###the spelling mistakes are identified and corrected using fuzzywuzzy library; and are mapped to correct spellings
###the articles that are not found (mapped to '') are assigned the subject category i.e C0001

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



Q11) execute category-ratios-generator.sh : Output: category-ratios.csv
[category pairs considered for subtree also] 
