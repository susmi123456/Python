#how to  invoke inner function from outerside
def add():
    print("Addition")

x= add
print(x) #<function add at 0x0000022EF277CA40>
x() #Addition
x() #Addition
x() #Addition
