a=10
b=20   #global scope
def wish():
    a=100   #local scope
    b=200
    print(a)  #100


wish()
print(a+b)  #30