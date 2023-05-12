# function that is divisible by 7,using the for loop. 
# return a list containing all the numbers between 100 and 200 that are divisible by 7

def divisible_by_7():
    emptyArr=[]
    for i in range(100,201):
        if i%7==0:
            emptyArr.append(i)
        return emptyArr

nums=[50,90,12,150,200,210]
print(divisible_by_7(nums))


# Write a function that accepts a list of unsorted intergers and return the smallest number in the list 
# E.G  smallest([3,6,8,2,4,1,5,7])
# return 1
# def smallest_num(list):
#     smallest=list[0]
#     for i in list:
#         if i<smallest:
#             smallest=i
#         return smallest
# nums=[2,4,3,5,67,8]
# print(smallest_num(nums))

# function that takes one arguments as a list a=[2,6,8] and remove the second last item
def remove_tem(item):
    item.pop(-2)
    return item
a=[2,6,8]
print(remove_tem(a))

#python functions that takes two inputs (integers) from a user and adds the two numbers,
#  check if the sum is greater than 10, less than 10 or equal 10 and prints a statement after each box
def integers(num1,num2):
    sum=num1+num2
    if sum>10:
        print("sum greater than 10")
    elif sum<10:
        print("sum less than 10")
    else:
        print("equal to 10")
nums=[1,2,3,5,6,8]
integers(12,5)

# python function that takes one argument which is a list , 
# a=[1,2,3,4,5] and return true if 4 is present in the list and False is 4 is not in the in the list
def numbers(num):
    if 4 in num:
        return True
    else:
        return False
a=[1,2,3,4,5]
print(numbers(a))

# python functions that takes one argument which is a list  
# fruits=["apple","grape","pineaple"] and remove the last fruits 
# from the list then return the list without the removed fruit
def remove_fruit(list):
    
    fruits.pop()
    return fruits

fruits=["apple","grape","pineaple"]
update=remove_fruit(fruits)
print(update)

# python function that takes in a list of cars,cars=["Ford","BMW","Volvo"] and return a sorted list
def car_list(car):
    return sorted(car)

cars=["Ford","BMW","Volvo"]
print(car_list(cars))


# 

    

    



     