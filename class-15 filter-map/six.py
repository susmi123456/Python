numbers=[10,78,14,96,117,11,31,42]
print(numbers)
# def check(num):
#     return num%2 ==0
    
even_numbers=list(filter(lambda num:num%2 ==0,numbers))
print(even_numbers)