class Account:
    def __init__(self,id,name):
        self.acc_id=id
        self.acc_name=name
        self.acc_bal=0
    def deposite_amount(self,amount):
        self.acc_bal=self.acc_bal+amount

a1=Account(11,'Rahul')
print(a1.__dict__)
a1.deposite_amount(5000)
a1.deposite_amount(500)
a1.deposite_amount(50)
a1.deposite_amount(50)
print(a1.__dict__)

a2=Account(12,'Sonia')
print(a2.__dict__)
a2.deposite_amount(500000)
a2.deposite_amount(1)
print(a2.__dict__)