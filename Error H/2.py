from BalError import InsuffiantBalError

amount=int(input("Enter Amount:"))
acc_Bal = 15000

if acc_Bal < amount:
    #print("Low Balance")
    raise InsuffiantBalError("Low Balance")
else:
    print("Withdrawl and Enjoy")

print("good morning")