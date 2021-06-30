import numpy as np
import xlrd
from collections import Counter
def open_excel(fileName="20200508 cleaned capitaliq agrifood.xlsx"):
    try:
        fileHandler = xlrd.open_workbook(fileName)
        return fileHandler
    except Exception as e:
        print(str(e))  
def scan_excel(sheet_name1='Sheet2'):
    handler = open_excel()
    page = handler.sheet_by_name(sheet_name1)
    return page
def trim_cols(index=0):
    page = scan_excel()
    col = page.col_values(index)
    num_col=Counter(col)
    for i in num_col:
        a = []
        a.extend(i)
        a.insert(0,'.')
        a.insert(0,'w')
        a.insert(0,'w')
        a.insert(0,'w')
        print(''.join(a))
def main():
    trim_cols()
if __name__ == "__main__":
    main()


######### To discard the 'nan' term #########
for values in dict_company.values():
  vl = []
  for value in values.values():
    vl.append(value)
    vl = [value for value in vl if str(value) != 'nan']
  #print(vl)
  for column in vl:
    print(df1[[column]])
