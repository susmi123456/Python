def smart_div(func):

    def inner(a,b):
        if b==0:
            print("Can't DIviside by Zero")
        else:
            func(a,b)
            
    return inner


def calc(a,b):
    print(a/b)


calc(10,2) #5.0
calc(10,5) #2.0
calc(10,0)  #ZeroDivisionError: division by zero
calc(10,1)  #stop the execution