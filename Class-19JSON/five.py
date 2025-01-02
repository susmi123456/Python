import json
fp=open("employee.json","r")
employees=json.load(fp)
print(type(employees))
print(len(employees))
print(employees)

Male_emp=[]
for emp in employees:
    if emp['gender']=='Male':
        #print(emp['ename'])
        Male_emp.append(emp)

fp2=open("male.json",'w')
json.dump(Male_emp,fp2)
print("new file crated successfully")