fp=open('data.txt','r')

print(fp.name)
print(fp.readable())
print(fp.writable())
print(fp.closed)
fp.close()
print(fp.closed)