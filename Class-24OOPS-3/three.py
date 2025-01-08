class Account:
    min_bal=500
    def __init__(self,id,name):
        self.acc_id=id
        self.acc_name=name
        self.acc_bal=0
    def deposite_amount(self,amount):
        self.acc_bal=self.acc_bal+amount

    def withdrawl(self,amount):
        self.acc_bal=self.acc_bal-amount

    def get_bal(self):
        bal=self.acc_bal-self.min_bal
        return bal

a1=Account(11,'Rahul')
a1.deposite_amount(5000)

a2=Account(12,'Sonia')
a2.deposite_amount(500000)
a2.deposite_amount(1)

a1.withdrawl(15)

print("******Account holders balance******")
print("Account")
print(Account.__dict__)
print(a1.__dict__)
print(a2.__dict__)