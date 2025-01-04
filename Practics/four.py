class Test:
    def __init__(self,a,b):
        print(a,b)
        print("contraction ")

    def m1():
        print("instance method - m1")
    @classmethod
    def m2():
        print("class method -m2")

t1=Test(10,20)
t2=Test(100,200)