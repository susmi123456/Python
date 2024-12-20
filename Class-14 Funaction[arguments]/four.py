def cal(a,b,c=100):
    print(a+b+c)

cal(1,2,3) #6
cal(1,2)  #TypeError: cal() missing 1 required positional argument: 'c'