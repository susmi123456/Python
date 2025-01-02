import json
fp=open("employee.json","r")
employees=json.load(fp)
print(type(employees))
print(len(employees))
print(employees)


for emp in employees:
    if emp['gender']=='Female':
        print(emp['ename'])