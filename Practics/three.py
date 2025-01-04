class Person:
    def __init__(self,id,name,age,sal):
        self.id=id
        self.name=name
        self.age=age
        self.sal=sal

a1= Person(101,"Rahul",20,25000)
a2= Person(102,"sonia",25,5000)

print(a1.__dict__)
print(a2.__dict__)
        