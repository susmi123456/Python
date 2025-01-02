fp=None
try:
    fp=open('emp.json','r')
    data=fp.read()
    a = int(input("Enter Fisrst Number"))
    b = int(input("Enter Second Number"))
    print(a+b)
except TypeError as te:
    print("Type Mismatch")
except FileNotFoundError as fnt:
    fp=open("default.json","w")

except ValueError as ve:
    print("Unable to convert")
finally:
    print("finally Block will execute always")
    fp.close()

