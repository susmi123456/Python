class Account:
    def __init__(self,a,b,c):
        self.acc_id=a
        self.acc_name=b
        self.acc_bal=c


a1=Account(101,'Rahul',1500)
a2=Account(102,'Gandhi',5000)
print(a1.__dict__)
print(a2.__dict__)