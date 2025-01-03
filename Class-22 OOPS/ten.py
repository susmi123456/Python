class Test:
    '''Good Evending'''
    a=100          #static variable/class level
    b=200          #static variable/class level
    def m1(self):
        self.c=300  #instance variable

t1=Test()
print(Test.__dict__)  

'''
{'__module__': '__main__',
 '__doc__': 'Good Evending',
  'a': 100, 'b': 200, 
  'm1': <function Test.m1 at 0x0000019BABADD260>, 
  '__dict__': <attribute '__dict__' of 'Test' objects>, 
  '__weakref__': <attribute '__weakref__' of 'Test' objects>}
'''