#import datetime
#print(datetime.date)

from datetime import datetime as cdt

print(cdt.now().time())
print(cdt.now().year)
print(cdt.now().month)
print(cdt.now().date())
print(cdt.now().hour)
print(cdt.now().minute)
print(cdt.now().second)
print(cdt.now().microsecond)