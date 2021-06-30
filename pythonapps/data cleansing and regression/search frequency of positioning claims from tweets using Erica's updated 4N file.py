##### Import data to be cleaned and organized #####
import pandas as pd
#df = pd.read_csv("/Users/caiyizhao/Desktop/Chan's thesis project/Data files/combined_csv_2019_twitter1 copy.csv", usecols = ['tweet_cleaned', 'compound', 'likes_count', 'retweets_count', 'replies_count', 'date', 'urls', 'hashtags', 'photos', 'video'])
df = pd.read_excel("/Users/caiyizhao/Desktop/Chan's thesis project/Data files/combined_csv_2019_twitter1 ok.xlsx", usecols = ['tweet'])
df1 = pd.read_excel("/Users/caiyizhao/Desktop/Chan's thesis project/Data files/Erica/210323 Edited Format Erica’s 4N Value keywords read to use.xlsx", usecols = ['PM- Religion','CP&FV - Shifting demographic','CP&FV- Desire for more information about food','CP&FV- Naturalness','CP&FV- Taste','CP&FV- Convenience','CP&FV- Nutrition','FI- Enhanced nutrition profile','FI- Food additives','FI- Replacement ingredients','FI- Functional foods','MKT- Sustainability','MKT- Assurence standards','SFS- Economic sustainability','SFS- Social sustainability','SFS- Environmental sustainability','Close to nature','Nature','Man-Made','Sustainable Behaviours'])
df = df[['tweet']]
df1 = df1[['PM- Religion','CP&FV - Shifting demographic','CP&FV- Desire for more information about food','CP&FV- Naturalness','CP&FV- Taste','CP&FV- Convenience','CP&FV- Nutrition','FI- Enhanced nutrition profile','FI- Food additives','FI- Replacement ingredients','FI- Functional foods','MKT- Sustainability','MKT- Assurence standards','SFS- Economic sustainability','SFS- Social sustainability','SFS- Environmental sustainability','Close to nature','Nature','Man-Made','Sustainable Behaviours']]

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
        #print('0')
        list5.append('0')
print('allergen:'+str(list5.count('1')))
df['allergen'] = list5

list6 = []
for i in df['tweet']:
    if 'additive' in str(i).lower():
        #print('1')
        list6.append('1')
    else:
        #print('0')
        list6.append('0')
print('additive:'+str(list6.count('1')))
df['additive'] = list6

list7 = []
for i in df['tweet']:
    if 'preservative' in str(i).lower():
        #print('1')
        list7.append('1')
    else:
        #print('0')
        list7.append('0')
print('preservative:'+str(list7.count('1')))
df['preservative'] = list7

list8 = []
for i in df['tweet']:
    if 'kosher' in str(i).lower():
        #print('1')
        list8.append('1')
    else:
        #print('0')
        list8.append('0')
print('kosher:'+str(list8.count('1')))
df['kosher'] = list8

list9 = []
for i in df['tweet']:
    if 'transfat' in str(i).lower():
        #print('1')
        list9.append('1')
    else:
        #print('0')
        list9.append('0')
print('transfat:'+str(list9.count('1')))
df['transfat'] = list9

list10 = []
for i in df['tweet']:
    if 'cholesterol' in str(i).lower():
        #print('1')
        list10.append('1')
    else:
        #print('0')
        list10.append('0')
print('cholesterol:'+str(list10.count('1')))
df['cholesterol'] = list10

list11 = []
for i in df['tweet']:
    if 'sodium' in str(i).lower():
        #print('1')
        list11.append('1')
    else:
        #print('0')
        list11.append('0')
print('sodium:'+str(list11.count('1')))
df['sodium'] = list11


for column in df1.iteritems():
    for i in column:
        for j in i:
            group = 0
            if j == 'nan':
                pass
            else:
                for q in df['tweet']:
                    if str(j) in str(q).lower():
                        group = group + 1
                    else:
                        group = group
                print(str(j)+":"+str(group))
                




#print(df)
#df.to_csv(r"/Users/caiyizhao/Desktop/Chan's thesis project/Data files/combined_csv_2019_twitter1 ok.csv", index = False, header=True)
#df.to_excel (r"/Users/caiyizhao/Desktop/Chan's thesis project/Data files/combined_csv_2019_twitter1 ok.xlsx", index = False, header=True)