import csv
import json
fp1=open('emp.json','r')
fp2=open('emp.csv','w',newline='')
employees=json.load(fp1)
print(employees)


fp1.close()
fp2.close()