def change_case(func):
    
    def inner(name):
        return func(name.upper())
    
    return inner

def greet(name):
    print("Hi",name)


greet("rahul")  #rahul
greet("modi")   #modi