# Write a Python function that takes two arguments (a and b) and returns their sum.
def addition(a,b):
    sum=a+b
    return sum

print(addition(12,6))

# Write a Python function that takes a string as input and returns the string reversed.
def reversedString(str):
    empty=""
    for i in range(len(str)-1,-1,-1):
        empty+=str[i]
    return empty
print(reversedString("Marisah"))
        
# Write a Python function that takes a list of integers as input and returns the sum of all the integers in the list.
def integers(int):
    sum=0
    for i in int:
        sum+=i
    return sum
nums= [2,3,4,10,12]
print(integers(nums))


# Write a Python function that takes a list of integers as input and returns a new list with all the even numbers removed.
def even_numbers(*new):
    newArr=[]
    for i in new:
        if i%2!=0:
            newArr.append(i)
    return newArr

print(even_numbers(1,2,4,5,6,8,9))

# Write a Python function that takes a list of integers as input and returns the highest value in the list.

def highest_values(*lst):
    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value
print(highest_values(1,2,4,5,8,7,12))

# Write a Python function that takes a list of strings as input and returns a new list with all the strings capitalized.
def listIntegers(str):
    return str.capitalize()
print(listIntegers("akiraChix"))