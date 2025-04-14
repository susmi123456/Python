class Account:
    '''class is created by susmitha'''
    def open_account(self):
        print("Account opened succssfully")
    def deposit_amount(self):
        print("Amount deposited")
    def withdrawl(self):
        print("Amount withdrawl")

a1=Account()
a2=Account()
#printing object  in the from of dict
print(a1.__dict__) #{}
print(a2.__dict__)  #{}
print(Account.__dict__)