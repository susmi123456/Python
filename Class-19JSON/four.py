import json
fp=open("employee.json","r")
employees=json.load(fp)
print(type(employees))
print(len(employees))
print(employees)

female_emp=[]
for emp in employees:
    if emp['gender']=='Female':
        
        female_emp.append(emp)

fp2=open('female.json','w')
json.dump(female_emp,fp2)
print("New File Crated Successfully")