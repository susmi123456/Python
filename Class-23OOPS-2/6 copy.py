class Account:
    def __init__(self,id,name,amount):
        self.acc_id=id
        self.acc_name=name
        self.acc_bal=amount
    # def deposit_account(self,amount):
    #     self.acc_bal=self.acc_bal + amount
    # def Withdral(self,amount):
    #     self.acc_bal=self.acc_bal - amount


a1=Account(101,'Rahul',5000)
a2=Account(102,'Sonia',50000)
print(a1.__dict__)
print(a2.__dict__)
# a1.deposit_account(15000)
# a2.deposit_account(150)
# print(a1.__dict__)
# a1.Withdral(15)

# print(a1.__dict__)
