import json
emp_str='''{"eid": 101, "ename": "Rahul", "esal": 45000.45, "avail": true, "loc": null}'''

emp_dict=json.loads(emp_str)
print(emp_dict)

# import json
# emp_str='''{'eid': 101, "ename": "Rahul", "esal": 45000.45, "avail": true, "loc": null}'''

# emp_dict=json.loads(emp_str)
# print(emp_dict)


# loads()--> json to python object
# dumps()--> python object to json object