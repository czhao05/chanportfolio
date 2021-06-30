import csv
import pandas as pd
df = pd.read_csv("/Users/caiyizhao/Desktop/Chan's thesis project/Data files/Yang_combined_20210315.csv")
#df = pd.read_excel("/Users/caiyizhao/Desktop/Chan's thesis project/Data files/combined_csv_2019_twitter1.xlsx")
tweets = df['Text Content']
#for row in data:    #This is for csv 
    #rowtweet = row['tweet']
    #tweets.append(rowtweet)
print(len(tweets))
##### remove punctuations #####
import re
tweets2=[]
for i in tweets:
    a = re.sub(r'[^\w\s]','', str(i))
    #print(a)
    tweets2.append([a])
#print(tweets2)

##### tokenization & stop word removal#####
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords  
from nltk.tokenize import word_tokenize  
stop_words = set(stopwords.words('english'))
tweets3=[]
for j in tweets2:  
    b = word_tokenize(str(j)) 
    filtered_sentence = [w for w in b if not w in stop_words]    
    filtered_sentence = [] 
    for w in b:  
        if w not in stop_words:  
            filtered_sentence.append(w)
    tweets3.append(filtered_sentence) 
    #print(b)  
#print(str(tweets3)[1:-1][1:-1])

##### lemmatization #####
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
ltz = WordNetLemmatizer()
tweets4=[]
for q in tweets3:
    c = ' '.join([ltz.lemmatize(d)for d in q])
    tweets4.append(c)
#print(tweets4)

##### Convert tweets5 into dataframe #####
import pandas as pd
df = pd.DataFrame(tweets4)
df.columns=['tweet_cleaned']
#print(df)

##### Sentiment Analysis #####
# Because we don't have the convenience to make a well-labeled training dataset that includes enough samples labeled by "positive", "negative", and "neutral", we will have to use lexicon-based sentiment analysis.
# Because VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based sentiment analysis tool that's for sentiments expressed in social media.
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
sid.polarity_scores('I would definately recommend this one')

##### prepare for to convert output of the vader_lexicon to list #####
def dict_converter(dict1):
  dictlist = list()
  for key, value in dict1.items():
    temp = [key,value]
    dictlist.append(temp)
  return dictlist

##### sentiment analysis #####
ttt = list()
for e in df['tweet_cleaned']:
  dict_res = dict_converter(sid.polarity_scores(e))
  #nltk.sentiment.util.demo_vader_instance(_)
  ttt.append([e, dict_res[0][1], dict_res[1][1], dict_res[2][1], dict_res[3][1]])
ttt = pd.DataFrame(ttt)
ttt.columns = ['tweet_cleaned', 'neg', 'neu', 'pos', 'compound']
##### make new excel including the cleaned tweets and compound
df1 = pd.read_csv("/Users/caiyizhao/Desktop/Chan's thesis project/Data files/Yang_combined_20210315.csv")
new_df = pd.concat([df1,ttt],axis=1)
#print(ttt)

##### export data frame with existing twitter data file #####
#ttt.to_csv("/Users/caiyizhao/Desktop/Chan's thesis project/twitter_1_2019_1 copy.csv", header = True)
#aFile = open("/Users/caiyizhao/Desktop/Chan's thesis project/twitter_1_2019_1.csv", 'r')
#aInfo = csv.reader(aFile)
#bfile = open("/Users/caiyizhao/Desktop/Chan's thesis project/twitter_1_2019_1 copy.csv", 'r')
#bInfo = csv.reader(bfile)
#cfile = open("/Users/caiyizhao/Desktop/Chan's thesis project/1_2019_1.csv", 'w')
#abcsv = csv.writer(cfile, dialect='excel')
#a=[]
#a=list()
#b=[]
#b=list()

#for info in aInfo:
    #a.append(info)

#for info in bInfo:
    #b.append(info)

#for index in range(len(b)):  
    #a[index].extend(b[index])
    #abcsv.writerow(a[index])

#writer = pd.ExcelWriter("/Users/caiyizhao/Desktop/Chan's thesis project/Data files/Twitter_Ye_2020_Combined_All_1-26 copy.csv") 
new_df.to_csv(r"/Users/caiyizhao/Desktop/Chan's thesis project/Data files/Yang_combined_20210315 copy.csv", index = False)
#new_df.to_excel(writer, index = False, sheet_name='in')
#writer.save()