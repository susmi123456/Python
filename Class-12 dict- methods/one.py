employee={
    'eid':101,
    'ename':'Rahul',
    'esal':4500,
    'eloc':['Wayanad',"New Delhi","Noida"],
    'address':{
        'city':'Bangalore',
        'Pincode':560037
    }
}
print(employee.keys())

for key in employee.keys():
    print(key)

#o/p
# dict_keys(['eid', 'ename', 'esal', 'eloc', 'address'])
# eid
# ename
# esal
# eloc
# address
