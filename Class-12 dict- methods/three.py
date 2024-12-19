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
for item in employee.items():
    print(item)

#o/p
# ('eid', 101)
# ('ename', 'Rahul')
# ('esal', 4500)
# ('eloc', ['Wayanad', 'New Delhi', 'Noida'])
# ('address', {'city': 'Bangalore', 'Pincode': 560037})


