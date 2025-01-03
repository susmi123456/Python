class Account:
    acc_min_bal = 500
    branch_name = "marthahalli"

    def open_account(self):
        print("Account Opened Successfuly")
    def deposit_account(self):
        print("Amount Deposited")
    def withdrawl_account(self):
        print("Low Balance")
    def close_account(self):
        print("bal is -ve! plase deposit more")


a1=Account()
a2=Account()
print(a1)
print(type(a1))
print(id(a1))