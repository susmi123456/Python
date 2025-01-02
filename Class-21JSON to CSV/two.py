import csv
import json
fp1=open('emp.json','r')
fp2=open('emp.csv','w',newline='')
employees=json.load(fp1)
employees_list=[]

for emp in employees:
    #employees_list.append(list())
    employees_list.append([emp['eid'],emp['ename'],emp['gender']])
csvwriter=csv.writer(fp2)
csvwriter.writerow(['eid','ename','gender'])
csvwriter.writerows(employees_list)
#print(employees_list)   
fp1.close()
fp2.close()