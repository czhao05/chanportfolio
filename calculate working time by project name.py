import pandas as pd
df = pd.read_excel('/Users/caiyizhao/Desktop/LianLiu_2021_1623372329.xlsx', sheet_name = 'lianliu_2021', header = 2, usecols= ['Project','Time Est.'])
#print(df)
df.dropna(subset=['Project','Time Est.'], inplace=True)
#print(df)
df1 = df[df.iloc[:, 0] != df.columns[0]]
#print(df1)
project=df1['Project'].drop_duplicates()
print(project)
df1 = df1.groupby(['Project'], as_index=False)['Time Est.'].sum()      
print(df1)
#df1.to_excel('/Users/caiyizhao/Desktop/Lianliu worktime.xlsx')