class Account:
    def __init__(self):
        print("constractor is crated")
    def m1():
        print("instance method  - m1")
    @classmethod
    def m2():
        print("class method - m2")
    @staticmethod
    def m3():
        print("static method - m3")



a1=Account()
a2=Account()
a3=Account()