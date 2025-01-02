
try:
    a = int(input("Enter Fisrst Number"))
    b = int(input("Enter Second Number"))
    print(a+b+"Rahul")
    fp=open('emp.json','r')
    data=fp.read()
    print(data)
except TypeError as te:
    print("Type Mismatch")


except ValueError as ve:
    print("Unable to convert")
finally:
    print("finally Block will execute always")
fp.close()

