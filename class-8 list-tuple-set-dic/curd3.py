# eids=[]
# uids=[101,102,101,"Rahul

enames=['Rahul','Sonia','Priyaka','Modi']
#index    0      1         2       3
#-veindex  -4    -3        -2      -1
print(enames)
# how to read list elements - using indexing
#upadate list elements
enames[3]= "PM Naredra Modi"
print(enames)
#delete  list elements
enames.pop() #['Rahul', 'Sonia', 'Priyaka', 'PM Naredra Modi']
print(enames) #['Rahul', 'Sonia', 'Priyaka']
