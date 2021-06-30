import pandas as pd
df = pd.read_csv("/Users/caiyizhao/Desktop/Chan's thesis project/Data files/data 0413/AllTweetData_With_Users_20210402_Updated ok 0420.csv", usecols = ['likes','replies','retweet','retweet_count','soriginal','url','hashtag','photo','video','year19','year20','January','February','March','April','May','June','July','August','September','October','November','December','length','length_square','Q12019','Q22019','Q32019','Q42019','Q12020','Q22020','Q32020','Q42020','pos','neg','neu','organic','gluten','gmo','new','innovative','innovation','allergen','additive','preservative','kosher','transfat','cholesterol','sodium','food','covid'])

##### Set dependent and independent variables #####
import numpy as np
df['log_length'] = np.log(df['length'])
df['log(likes+1)'] = np.log(df['likes']+1)
df['log(replies+1)'] = np.log(df['replies']+1)
#print(df['log_length'])

##### Combine photo and video, combine innovative and innovation #####
df['phovideo'] = df['photo'] | df['video']
#print(df['phovideo'])
df['innovative/tion'] = df['innovative'] | df['innovation']
df['presertive'] = df['additive'] | df['preservative']

##### Build retweet dataframe #####
#print(df['retweet'])
dfnoretweet = df[df['retweet']==0]
#print(dfnoretweet)
df19noretweet = dfnoretweet[dfnoretweet['year19']==1]
df20noretweet = dfnoretweet[dfnoretweet['year20']==1]
#print(df19noretweet) ##### When retweet = 1, all likes are 0. (including both 2019 and 2020)
#print(df20noretweet)

##### Build 2019 and 2020 file seperately #####
df2019 = df[df['year19']==1]
#print(df2019)
df2019likes = df2019[df2019['likes']!=0]
df2019nolikes = df2019[df2019['likes']==0]

dfinno2019 = df2019[df2019['innovative/tion']==1]
dfnoinno2019 = df2019[df2019['innovative/tion']==0]

#print(len(df2020likes))
#df2019.to_csv(r"/Users/caiyizhao/Desktop/Chan's thesis project/Data files/AllTweetData_2019file.csv", index = False, header=True)
df2020 = df[df['year20']==1]
dfinno2020 = df2020[df2020['innovative/tion']==1]
dfnoinno2020 = df2020[df2020['innovative/tion']==0]
df2020likes=df2020[df2020['likes']!=0]
df2020nolikes=df2020[df2020['likes']==0]
#print(len(df2019))
#df2020.to_csv(r"/Users/caiyizhao/Desktop/Chan's thesis project/Data files/AllTweetData_2020file.csv", index = False, header=True)
###df20no_covid = df2020[df2020['covid'] == 0]
#df20no_covid.to_csv(r"/Users/caiyizhao/Desktop/Chan's thesis project/Data files/AllTweetData_2020no_covidfile ok.csv", index = False, header=True)

##### GLM #####
import statsmodels.api as sm
##Poisson##
#count_model = sm.GLM(df2019['likes'], 
#sm.add_constant(df2020[['pos','neg','url','hashtag','phovideo','length_square','Q22020','Q32020','Q42020','organic','gluten','gmo','allergen','presertive','kosher','transfat','cholesterol','sodium','covid','retweet_count']]),
#family=sm.families.Poisson(sm.genmod.families.links.log)).fit()
#summary = count_model.summary()
#print(summary)

#dfinno2019.to_csv(r"/Users/caiyizhao/Desktop/Chan's thesis project/Notes/2019inno.csv", index = False, header=True)
##Negative Binomial## 
model = sm.GLM(dfinno2019['likes'],sm.add_constant(dfinno2019[['soriginal','url','hashtag','phovideo','Q12019','Q22019','Q32019','organic','gluten','gmo','new','kosher','allergen','presertive','food','length_square']]),family=sm.families.NegativeBinomial(sm.genmod.families.links.log)).fit()
print(model.summary())

## Check correlation ##
corr = df.corr()
#corr.to_csv(r"/Users/caiyizhao/Desktop/Chan's thesis project/Notes/corr 061421.csv", index = True, header=True)


#'Q12019','Q22019','Q32019'
#'Q22020','Q32020','Q42020'
#'organic','gluten','gmo','new','innovative/tion','allergen','presertive','kosher','transfat','cholesterol','sodium','food','covid'
#X = dfnoretweet[['pos','neg','url','hashtag','phovideo','log_length','Q22020','Q32020','Q42020','organic','gluten','gmo','allergen','presertive','kosher','transfat','cholesterol','sodium','covid','retweet_count']]


##### Check if standardized #####
###X1_norm.columns = df2019.columns
###X1_norm = sm.add_constant(X1_norm) 
###check = pd.concat([round(X1_norm.mean(axis=0), 5), round(X1_norm.std(axis=0, ddof=0), 5)], axis=1)
###check.columns=["mean", "std dev"]
###print(check)


############## Because the condition number is very large, there might be multicollinearity problem ############
from statsmodels.stats.outliers_influence import variance_inflation_factor

X = dfinno2019[['soriginal','url','hashtag','phovideo','Q12019','Q22019','Q32019','organic','gluten','gmo','new','kosher','allergen','presertive','food','length_square']]

def calc_vif(X):

    #####Calculating VIF #####
    vif = pd.DataFrame()
    vif['soriginal','url','hashtag','phovideo','Q12019','Q22019','Q32019','organic','gluten','gmo','new','kosher','allergen','presertive','food','length_square'] = X.columns
    #'February','March','April','May','June','July','August','September','October','November','December'
    vif["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

    return(vif)

print(calc_vif(X))

######### ANOVA #########
#import statsmodels.api as sm
#from statsmodels.formula.api import ols
#df3.boxplot('dependent', by = 'indepedent')
#mod = ols('dependent ~ independent', data = df3).fit()
#aov_table = sm.stats.anova_lm(mod, typ=2)
#print(aov_table)

########### Logit Regression (while the dependent variables are not binary)############
#df3['log_ltr'] = np.log(df3['likes']+df3['retweets']+df3['replies'])
##r = float(df3['soriginal'][-1] - df3['soriginal'][0])
##normal = map(lambda x: (x - df3['soriginal'][0]) / r, df3['soriginal'])
#print(df3['log_ltr'])
##print(normal)
#X = df3[['soriginal','log_length','url', 'hashtag', 'photo', 'month']]
#X = sm.add_constant(X) # adding a constant
#Y2 = df3['log_ltr'] 
#model_log = sm.OLS(Y2, X).fit()
#predictions1 = model_log.predict(X) 
#print_model = model_log.summary()
#print(print_model)

############ Logit Regression (while the dependent variables are binary)###########
#y = df3['likes']
#x = df3[['soriginal','url', 'hashtag', 'photo', 'month']]
#model_logit = sm.Logit(y, x)
#result = model_logit.fit(method='newton')
#result.predict(x)
#logit_result = result.summary()
#logit_result2 = result.summary2()
#print('This is logit regression' + str(logit_result))
#print(logit_result2)