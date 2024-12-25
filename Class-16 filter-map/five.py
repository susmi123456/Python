# prices=[100,200,300]
# total= reduce(lambda a,b:a+b,prices)
# print(total)  #NameError: name 'reduce' is not defined

# from functools import reduce
# prices=[100,200,300]
# total= reduce(lambda a,b:a+b,prices)
# print(total) 

from functools import reduce

prices=[100,200,300]

result=0
def sumof(a,b):
    return a+b

total= reduce(sumof,prices)
print(total) 