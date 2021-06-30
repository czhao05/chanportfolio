##### Import data to be cleaned and organized #####
import pandas as pd
df = pd.read_csv("/Users/caiyizhao/Desktop/Chan's thesis project/Data files/Yang_combined_20210315 copy.csv", usecols = ['tweet_cleaned', 'compound', 'Favorites #', 'Retweets #', 'Date Time'])
#df = pd.read_excel("/Users/caiyizhao/Desktop/Chan's thesis project/Data files/combined_csv_2019_twitter1 copy.xlsx", usecols = ['tweet_cleaned', 'compound', 'likes_count', 'retweets_count', 'replies_count', 'date', 'urls', 'hashtags', 'photos', 'video'])
#df = df[['tweet_cleaned', 'compound', 'likes_count', 'retweets_count', 'date']]
#print(df)

##### Get month from "date" #####
month = []
from datetime import datetime
for i in df['Date Time']:
    a = datetime.strptime(i,"%Y-%m-%d %H:%M")
    b = a.month
    month.append(b)
    print(b)
print(len(month))
df['month'] = month
df = df.drop(['Date Time'], axis = 1)
January = []
for i in df['month']:
    if int(i) == 1:
        x = 1
        January.append(x)
    else:
       x = 0
       January.append(x)
df['January']=January
print(df['January'])

February = []
for i in df['month']:
    if int(i) == 2:
        x = 1
        February.append(x)
    else:
       x = 0
       February.append(x)
df['February']=February

March = []
for i in df['month']:
    if int(i) == 3:
        x = 1
        March.append(x)
    else:
       x = 0
       March.append(x)
df['March']=March

April = []
for i in df['month']:
    if int(i) == 4:
        x = 1
        April.append(x)
    else:
       x = 0
       April.append(x)
df['April']=April

May = []
for i in df['month']:
    if int(i) == 5:
        x = 1
        May.append(x)
    else:
       x = 0
       May.append(x)
df['May']=May

June = []
for i in df['month']:
    if int(i) == 6:
        x = 1
        June.append(x)
    else:
       x = 0
       June.append(x)
df['June']=June

July = []
for i in df['month']:
    if int(i) == 7:
        x = 1
        July.append(x)
    else:
       x = 0
       July.append(x)
df['July']=July

August = []
for i in df['month']:
    if int(i) == 8:
        x = 1
        August.append(x)
    else:
       x = 0
       August.append(x)
df['August']=August

September = []
for i in df['month']:
    if int(i) == 9:
        x = 1
        September.append(x)
    else:
       x = 0
       September.append(x)
df['September']=September

October = []
for i in df['month']:
    if int(i) == 10:
        x = 1
        October.append(x)
    else:
       x = 0
       October.append(x)
df['October']=October

November = []
for i in df['month']:
    if int(i) == 11:
        x = 1
        November.append(x)
    else:
       x = 0
       November.append(x)
df['November']=November

December = []
for i in df['month']:
    if int(i) == 12:
        x = 1
        December.append(x)
    else:
       x = 0
       December.append(x)
df['December']=December

df = df.drop(['month'], axis = 1)
##### count the length of each tweet #####
df['length'] = df['tweet_cleaned'].str.split().str.len()-3
df['length_square'] = df['length']**2
#print(df)

##### change column names, so that all column names are exactly the name of the dependent and independent variables #####
df.columns = ['tweet', 'soriginal', 'likes', 'retweets', 'January','February','March','April','May','June','July','August','September','October','November','December','length','length_square']
#print(df)

##### Generate independent variables: allergen, gluten, additives, preservatives, kosher, transfat #####
print(len(df['tweet']))
#keywords = ['organic','new','innovative','innvoation','GMO']
list0 = []
for i in df['tweet']:
    if 'organic' in str(i).lower():
        #print('1')
        list0.append('1')
    else:
        #print('0')
        list0.append('0')
print('organic:'+str(list0.count('1')))
df['organic'] = list0

list1 = []
for i in df['tweet']:
    if 'gluten' in str(i).lower():
        #print('1')
        list1.append('1')
    else:
        #print('0')
        list1.append('0')
print('gluten:'+str(list1.count('1')))
df['gluten'] = list1

list2 = []
for i in df['tweet']:
    if 'gmo' in str(i).lower():
        #print('1')
        list2.append('1')
    else:
        #print('0')
        list2.append('0')
print('gmo:'+str(list2.count('1')))
df['gmo'] = list2

list1 = []
for i in df['tweet']:
    if 'new' in str(i).lower():
        #print('1')
        list1.append('1')
    else:
        #print('0')
        list1.append('0')
print('new:'+str(list1.count('1')))
df['new'] = list1

list3 = []
for i in df['tweet']:
    if 'innovative' in str(i).lower():
        #print('1')
        list3.append('1')
    else:
        #print('0')
        list3.append('0')
print('innovative:'+str(list3.count('1')))
df['innovative'] = list3

list4 = []
for i in df['tweet']:
    if 'innovation' in str(i).lower():
        #print('1')
        list4.append('1')
    else:
        #print('0')
        list4.append('0')
print('innovation:'+str(list4.count('1')))
df['innovation'] = list4

list5 = []
for i in df['tweet']:
    if 'allergen' in str(i).lower():
        ##print('1')
        list5.append('1')
    else:
        ##print('0')
        list5.append('0')
#print('allergen:'+str(list4.count('1')))
df['allergen'] = list5

list6 = []
for i in df['tweet']:
    if 'additive' in str(i).lower():
        ##print('1')
        list6.append('1')
    else:
        ##print('0')
        list6.append('0')
#print('allergen:'+str(list4.count('1')))
df['additive'] = list6

list7 = []
for i in df['tweet']:
    if 'preservative' in str(i).lower():
        ##print('1')
        list7.append('1')
    else:
        ##print('0')
        list7.append('0')
#print('allergen:'+str(list4.count('1')))
df['preservative'] = list7

list8 = []
for i in df['tweet']:
    if 'kosher' in str(i).lower():
        ##print('1')
        list8.append('1')
    else:
        ##print('0')
        list8.append('0')
#print('allergen:'+str(list4.count('1')))
df['kosher'] = list8

list9 = []
for i in df['tweet']:
    if 'transfat' in str(i).lower():
        ##print('1')
        list9.append('1')
    else:
        ##print('0')
        list9.append('0')
#print('allergen:'+str(list4.count('1')))
df['transfat'] = list9

list10 = []
for i in df['tweet']:
    if 'cholesterol' in str(i).lower():
        ##print('1')
        list10.append('1')
    else:
        ##print('0')
        list10.append('0')
#print('allergen:'+str(list4.count('1')))
df['cholesterol'] = list10

list11 = []
for i in df['tweet']:
    if 'sodium' in str(i).lower():
        ##print('1')
        list11.append('1')
    else:
        ##print('0')
        list11.append('0')
#print('allergen:'+str(list4.count('1')))
df['sodium'] = list11

print(df)
#df.to_csv(r"/Users/caiyizhao/Desktop/Chan's thesis project/Data files/Yang_combined_20210315 ok.csv", index = False, header=True)
#df.to_excel (r"/Users/caiyizhao/Desktop/Chan's thesis project/Data files/combined_csv_2019_twitter1 ok.xlsx", index = False, header=True)

