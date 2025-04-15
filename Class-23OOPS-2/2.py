class Account:
    '''claass created by Narasimha'''

    def open_account(self):
        print("Account opend successfully")
    def deposit_amount(self,amount):
        print("Amount Deposited successfully")
    @classmethod
    def update_min_bal(cls,amount):
         print("Min bal updated")
    @staticmethod
    def cal_interest():
        print("Utility method")

a1=Account()

a2=Account()
#how to Access class members? using object
a1.open_account()
a1.deposit_amount(5000)
a1.update_min_bal(600)
a1.cal_interest()

