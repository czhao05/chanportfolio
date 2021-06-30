import pandas as pd
df = pd.read_csv("/Users/caiyizhao/Desktop/Chan's thesis project/Data files/AllTweetData_With_Users_20210402_Updated ok2.csv")

##### Define the frequency function #####
def freq(str):
    str = str.split()
    list0 = []
    for i in str:
        if i not in list0:
            list0.append(i)
    for i in range(0,len(list0)):
        print('Frenqucy of', list0[i], 'is', str.count(list0[i]))

##### Merge all cells of 'tweet' column into one list for frequency checking #####
list5 = []
for i in df['tweet']:
    a = i.split()
    b = a[2:-2]
    list5.append(b)

def flatten_list(_2d_list):
    flat_list = []
    # Iterate through the outer list
    for element in _2d_list:
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list

final_list = flatten_list(list5)
#print(final_list)

##### Check the frequency #####
import csv
from collections import Counter
counts = Counter(final_list)
print(counts)
