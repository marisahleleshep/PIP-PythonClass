# Write a function that takes an unknown number of arguments and returns their sum.

def addition(*num):
    return sum(num)
print(addition(12,34,67,90))


# Write a function that takes two arguments, the first being a string and the 
# second being an unknown number of integers. The function should return a new 
# string where the integers have been added to the original string.
def integers(str,nums):
     result=0
     for num in nums:
           result +=str(nums)
           return result
     

integers("Hello Java",12)


# Write a function that takes an unknown number of keyword arguments and returns a 
# dictionary where the keys are the argument names and the values are the argument values.
def number_key(**kwargs):
     return kwargs
result= number_key(name="Rita",age=30,height=20.0)
print(result)


# Write a function that takes a function and an unknown number of arguments, 
# and returns the result of calling the function with the arguments.
def numbers_args(func, *args):
     result=func(*args)
     return result


def multiply(a, b):
    return a * b


def parameters(a,b):
     return a+b
result=number_key(parameters,12,8)
print(result)
    

     
     


# Write a function that takes a list of integers and an unknown number of keyword arguments.
#  The function should return a new list where each integer in the original list has been 
# multiplied by the value of the corresponding keyword argument.

def multiply_list(value, **kwargs):
    product = []
    for num in value:
        for key, value1 in kwargs.items():
            if int(key) == value.index(num):
                product.append(num * value)
    return product
print(multiply_list(12,2))


# Write a function that takes a list of integers and an unknown number of additional 
# integers as arguments. The function should return the index of the first 
# occurrence of the sum of the list and the additional integers

def find_sum_index(int, *args):
    sum_list = int + list(args)
    sum_value = sum(sum_list)
    for i in range(len(int_list)):
        if sum(int[:i+1]) == sum_value:
            return i
    return -1



# Write a function that takes an unknown number of keyword arguments, 
# each with a string value. The function should concatenate all the strings 
# and return the resulting string.

def unknown_keywords(**kwargs):
    result = ""
    for key, value in kwargs.items():
        result += value
    return result

result = unknown_keywords(a="Hello, ", b="world!")
print(result) 
     
