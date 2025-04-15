class Test:
    def __init__(self):
        print("Constrcutor is special method")
    def get_details(self):
        print("Instance method")
    @classmethod
    def update_Testclass(cls):
        print("class method")
    @staticmethod
    def sum(a,b):
        print("static method")

Test()
Test()