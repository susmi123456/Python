class Empolyee:
    ''' crated by a susmitha'''
    c=100 

    def m1(self):
        self.a=100
    def m2(self):
        self.b=200

e1=Empolyee()
e1.m1()
e2=Empolyee()
e2.m2()

print(e1.__dict__)
print(e2.__dict__)
print(Empolyee.__dict__)
