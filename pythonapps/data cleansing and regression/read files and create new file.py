import pandas as pd
import glob, os
inputpath = r'/Users/caiyizhao/Desktop/Innovation Ecosystem/Data-excels' #Insert path name here.
inputWorkbook=glob.glob(os.path.join(inputpath,"*.xlsx")) #Make sure all files are in .xlsx format. Also make sure the column name for all businesses and companies in files is "Company."
outputWorkbook='results.xlsx'
writer=pd.ExcelWriter(outputWorkbook)
for workbook in inputWorkbook:
    allData=[]
    combineData=pd.DataFrame()
    allSheetData=pd.read_excel(workbook,sheet_name=None)
    for name,data in allSheetData.items():
        allData.append(data)
        combineData=pd.concat(allData,axis=0,ignore_index=True)
        data=combineData.drop_duplicates('Company')
        data.to_excel(writer,sheet_name=os.path.basename(workbook),index=False)
        print(data)
writer.save()
        #company_url=data[['Company','URLs']]
        #company_url.to_excel(writer,sheet_name=os.path.basename('company_url'),index=False) #For now, only the last file gets scraped.
        #print(company_url)
        