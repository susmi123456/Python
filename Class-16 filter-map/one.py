
numbers = [10,150,70,230,130,30,500]
def check(ele):
    return ele<100

#filtered_data=filter(check,number)
filter_data=filter(lambda ele:ele<100,numbers)
print(type(filter_data))
result=list(filter_data)
print(result)
