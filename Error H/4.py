# print(10/0)

try:
    print(10/0)  #program creating Error
    # raise ZeroDivisionError("Go to Movie")
except ZeroDivisionError as err:
    print(err)