# a=int(input("Enter  frist number:"))
# b=int(input("Enter  second number:"))
# print(a/b)
# print('gm')

a=int(input("Enter  frist number:"))
b=int(input("Enter  second number:"))
try:
    print(a/b)
except ZeroDivisionError as error:
    print(a/1)
print('gm')