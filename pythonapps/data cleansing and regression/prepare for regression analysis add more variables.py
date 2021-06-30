##### Import data to be cleaned and organized #####
import pandas as pd
df = pd.read_csv("/Users/caiyizhao/Desktop/Chan's thesis project/Data files/data 0413/AllTweetData_With_Users_20210402_Updated copy.csv", usecols = ['tweet_cleaned', 'compound', 'likes_count', 'retweets_count', 'replies_count', 'date', 'urls', 'hashtags', 'photos', 'video'])
#df = pd.read_excel("/Users/caiyizhao/Desktop/Chan's thesis project/Data files/combined_csv_2019_twitter1 copy.xlsx", usecols = ['tweet_cleaned', 'compound', 'likes_count', 'retweets_count', 'replies_count', 'date', 'urls', 'hashtags', 'photos', 'video'])
df = df[['tweet_cleaned', 'compound', 'likes_count', 'retweets_count', 'replies_count','date', 'urls', 'hashtags', 'photos', 'video']]
#print(df)

##### Get Year #####
df['year'] = pd.DatetimeIndex(df['date']).year

year19 = []
for i in df['year']:
    if int(i) == 2019:
        x = 1
        year19.append(x)
    else:
        x = 0
        year19.append(x)
df['2019']=year19

year20 = []
for i in df['year']:
    if int(i) == 2020:
        x = 1
        year20.append(x)
    else:
        x = 0
        year20.append(x)
df['2020']=year20

##### Get month from "date" #####
df['month'] = pd.DatetimeIndex(df['date']).month

January = []
for i in df['month']:
    if int(i) == 1:
        x = 1
        January.append(x)
    else:
        x = 0
        January.append(x)
df['January']=January
#print(df1['January'])

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



df1 = df.drop(['date','month','year'], axis = 1)
##### count the length of each tweet #####
df1['length'] = df1['tweet_cleaned'].str.split().str.len()-3
df1['length_square'] = df1['length']**2
#print(df1)

##### make urls, hastags, photos, video all to binary variables #####
df1.urls[df['urls'] == '[]'] = 0
df1.urls[df['urls'] != '[]'] = 1
df1.hashtags[df['hashtags'] == '[]'] = 0
df1.hashtags[df['hashtags'] != '[]'] = 1
df1.photos[df['photos'] == '[]'] = 0
df1.photos[df['photos'] != '[]'] = 1

#print(df1)

##### change column names, so that all column names are exactly the name of the dependent and independent variables #####
df1.columns = ['tweet', 'soriginal', 'likes', 'retweets', 'replies', 'url', 'hashtag', 'photo', 'video','year19','year20','January','February','March','April','May','June','July','August','September','October','November','December','length','length_square']#
print(df1)

##### Generate independent variables: allergen, gluten, additives, preservatives, kosher, transfat #####
print(len(df1['tweet']))
#keywords = ['organic','new','innovative','innvoation','GMO']
list0 = []
for i in df1['tweet']:
    if 'organic' in str(i).lower():
        #print('1')
        list0.append('1')
    else:
        #print('0')
        list0.append('0')
print('organic:'+str(list0.count('1')))
df1['organic'] = list0

list1 = []
for i in df1['tweet']:
    if 'gluten' in str(i).lower():
        #print('1')
        list1.append('1')
    else:
        #print('0')
        list1.append('0')
print('gluten:'+str(list1.count('1')))
df1['gluten'] = list1

list2 = []
for i in df1['tweet']:
    if 'gmo' in str(i).lower():
        #print('1')
        list2.append('1')
    else:
        #print('0')
        list2.append('0')
print('gmo:'+str(list2.count('1')))
df1['gmo'] = list2

list1 = []
for i in df1['tweet']:
    if 'new' in str(i).lower():
        #print('1')
        list1.append('1')
    else:
        #print('0')
        list1.append('0')
print('new:'+str(list1.count('1')))
df1['new'] = list1

list3 = []
for i in df1['tweet']:
    if 'innovative' in str(i).lower():
        #print('1')
        list3.append('1')
    else:
        #print('0')
        list3.append('0')
print('innovative:'+str(list3.count('1')))
df1['innovative'] = list3

list4 = []
for i in df1['tweet']:
    if 'innovation' in str(i).lower():
        #print('1')
        list4.append('1')
    else:
        #print('0')
        list4.append('0')
print('innovation:'+str(list4.count('1')))
df1['innovation'] = list4

list5 = []
for i in df1['tweet']:
    if 'allergen' in str(i).lower():
        ##print('1')
        list5.append('1')
    else:
        #print('0')
        list5.append('0')
print('allergen:'+str(list5.count('1')))
df1['allergen'] = list5

list6 = []
for i in df1['tweet']:
    if 'additive' in str(i).lower():
        #print('1')
        list6.append('1')
    else:
        #print('0')
        list6.append('0')
print('additive:'+str(list6.count('1')))
df1['additive'] = list6

list7 = []
for i in df1['tweet']:
    if 'preservative' in str(i).lower():
        #print('1')
        list7.append('1')
    else:
        #print('0')
        list7.append('0')
print('preservative:'+str(list7.count('1')))
df1['preservative'] = list7

list8 = []
for i in df1['tweet']:
    if 'kosher' in str(i).lower():
        #print('1')
        list8.append('1')
    else:
        #print('0')
        list8.append('0')
print('kosher:'+str(list8.count('1')))
df1['kosher'] = list8

list9 = []
for i in df1['tweet']:
    if 'transfat' in str(i).lower():
        #print('1')
        list9.append('1')
    else:
        #print('0')
        list9.append('0')
print('transfat:'+str(list9.count('1')))
df1['transfat'] = list9

list10 = []
for i in df1['tweet']:
    if 'cholesterol' in str(i).lower():
        #print('1')
        list10.append('1')
    else:
        #print('0')
        list10.append('0')
print('cholesterol:'+str(list10.count('1')))
df1['cholesterol'] = list10

list11 = []
for i in df1['tweet']:
    if 'sodium' in str(i).lower():
        #print('1')
        list11.append('1')
    else:
        #print('0')
        list11.append('0')
print('sodium:'+str(list11.count('1')))
df1['sodium'] = list11

list12 = []
for i in df1['tweet']:
    if 'covid' in str(i).lower():
        #print('1')
        list12.append('1')
    else:
        #print('0')
        list12.append('0')
print('covid:'+str(list12.count('1')))
df1['covid'] = list12

list13 = []
for i in df1['tweet']:
    if 'help' in str(i).lower():
        #print('1')
        list13.append('1')
    else:
        #print('0')
        list13.append('0')
print('help:'+str(list13.count('1')))
df1['help'] = list13

list14 = []
for i in df1['tweet']:
    if 'thank' in str(i).lower():
        #print('1')
        list14.append('1')
    else:
        #print('0')
        list14.append('0')
print('thank:'+str(list14.count('1')))
df1['thank'] = list14

list15 = []
for i in df1['tweet']:
    if 'canada' in str(i).lower():
        #print('1')
        list15.append('1')
    else:
        #print('0')
        list15.append('0')
print('canada:'+str(list15.count('1')))
df1['canada'] = list15

list16 = []
for i in df1['tweet']:
    if 'food' in str(i).lower():
        #print('1')
        list16.append('1')
    else:
        #print('0')
        list16.append('0')
print('food:'+str(list16.count('1')))
df1['food'] = list16

print(df1)
df1.to_csv(r"/Users/caiyizhao/Desktop/Chan's thesis project/Data files/data 0413/AllTweetData_With_Users_20210402_Updated ok more variables.csv", index = False, header=True)
#df1.to_excel (r"/Users/caiyizhao/Desktop/Chan's thesis project/Data files/combined_csv_2019_twitter1 ok3.xlsx", index = False, header=True)

