class Employee:
    '''class crated by susmitha'''
    org_name="tcs"
    def __init__(self,id,name, sal):
        self.emp_id =id
        self.ename =name
        self.esal = sal

e1=Employee(101,"Rahul",45000.45)
e2=Employee(101,"Soniya",35000.55)
e3=Employee(101,"Priyaka",65000.85)
print(Employee.__dict__)
print(e1.__dict__)
print(e2.__dict__)
print(e3.__dict__)