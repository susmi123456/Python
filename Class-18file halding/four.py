fp1=open("data.txt",'r')
data=fp1.read()
print(data)
fp2=open("wish.txt",'w')
fp2.write(data)
print("New file created and written success")

fp1.close()
fp2.close()
