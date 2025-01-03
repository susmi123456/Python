class Account:
    acc_min_bal = 500
    branch_name = "marthahalli"

    def open_account(self):
        print("Account Opened Successfuly")
    def deposit_account(self):
        print("Amount Deposited")
    def withdrawl_account(self):
        print("Low Balance")
    def get_bal(self):
        print()
    def close_account(self):
        print("bal is -ve! plase deposit more")


a1=Account()
a1.open_account()
a1.deposit_account()
a1.withdrawl_account()
a1.get_bal()
a1.close_account()


