fp=open('data.txt','r+')

print("Before closing")
print(fp.closed)
fp.close()
print("After closing")
print(fp.closed)