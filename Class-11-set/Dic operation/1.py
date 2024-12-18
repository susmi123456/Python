# d1={}
# d2={1:'one',2:'two',3:'three'}
# d3={'email':'sri@gmail.com','email':'sri@ibm.com','email':'sri@oracal.com'}
# print(d1)
# print(d2)
# print(d3)

# emp = {
#     'eid':101,
#     'ename': 'Rahual',
#     'esal': 45000
# }
# print(emp.get('eid'))
# print(emp.get('ename'))
# print(emp.get('esal'))

# emp = {
#     'eid':101,
#     'ename': 'Rahual',
#     'esal': 45000
# }
# emp['ename'] ="Rahul Gandhi JI"
# emp['loc']= "wayanad"
# print(emp)

# emp ={'eid': 101, 'ename': 'Rahul Gandhi JI', 'esal': 45000, 'loc': 'wayanad'}
# del emp['esal']
# print(emp)

# employees=[
#           {'eid':101,'ename':'Rahul','gender':'Male'},
#           {'eid':102,'ename':'Sonia','gender':'Female'},
#           {'eid':103,'ename':'Priyanka','gender':'Female'},
#           {'eid':104,'ename':'Modi','gender':'Male'}
#           ]
# #print all employee names
# print(employees[0])
# print(employees[0].get('ename'))
# print(employees[1].get('ename'))
# print(employees[2].get('ename'))

employees=[
          {'eid':101,'ename':'Rahul','gender':'Male'},
          {'eid':102,'ename':'Sonia','gender':'Female'},
          {'eid':103,'ename':'Priyanka','gender':'Female'},
          {'eid':104,'ename':'Modi','gender':'Male'}
          ]
for employee in employees:
    print(employee.get('ename'))