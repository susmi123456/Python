fp=open("example.txt",'r')
data=fp.read()
print(data)
fp2=open("example.txt",'w')
data=fp2.write("hello akka")
print(data)
fp.close()
fp2.close()