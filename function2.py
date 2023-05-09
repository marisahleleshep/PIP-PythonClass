# Write a Python program to get a single string from two given strings, separated by a space, and swap 
# the first two characters of each string
def new_string(str1,str2):
    new1=str2[ :2]+str2[2: ]
    new2=str1[ :2]+str1[2: ]
    return new1 +' '+new2
print(new_string("Sammy","Mary"))


def singleString(string1,string2):
    new_string1=string2[ :3]+string1[3: ]
    new_string2=string1[ :1]+string2[1 :]
    return string1 +' '+string2
print(singleString("marisah","kelvin"))

<<<<<<< HEAD
# Write a Python function that takes a list of words and returns the longest word and the length of the longest one
=======
# #  Write a Python function that takes a list of words and returns the longest word and the length of the longest one
>>>>>>> 81881027840773dd0acbf01259fdc66cc6702fc9
def long_word(word):
    emptyArr=[]
    longest=0
    for i in word:
        if len(i)>longest:
            emptyArr=i
            longest=len(i)
    return longest,emptyArr

fruits=["apple","mango","lemon"]
print(long_word(fruits))

# # Write a Python program that accepts a comma-separated sequence of words 
# # as input and prints the distinct words in sorted form (alphanumerically).

words = input("Comma-separated sequence of words: ").split(",")
distinct_words = sorted(set(words))
print("Distinct words in sorted form:", ", ".join(distinct_words))



# def sort_words(input):
#     word_list=input.split(",")
#     word_set=set(word_list)
#     sorted_list=sorted(list(word_set))
#     return sorted_list
# fruits=["lemon","banana","juice"]
# print(sort_words(fruits))

# def sort_numbers(arr):
#     if len(arr)<=1:
#         return arr
#     mid=len(arr)//2
#     left=arr[ :mid]
#     right=arr[mid: ]

#     left=sort_numbers(left)
#     right=sort_numbers(right)

#     return mergeSort(left,right)

# def mergeSort(left,right):
#     emptyArr=[]
#     i=0
#     j=0
#     while i<len(left) and j<len(right):
#         if left[i]>right[j]:
#             emptyArr.append(left[i])
#             i+=1
#         else:
#             emptyArr.append(right[j])
#             j+=1

#             emptyArr+=left[i: ]
#             emptyArr+=right[ i:]
#             return emptyArr

# fruits=["apple","mango","lemon"]
# print(sort_numbers(fruits))


# # 4 Write a Python function that takes two lists and returns True if they have at least one common member.
def common_member(list,list1):
    for element in list:
        if element in list1:
            return True
    return False
list=["maria","lina","marina"]
list1=["janice","eve","maria"]

print(common_member(list,list1))


# # 5. Write a Python program to convert a list to a list of dictionaries.
# # Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
def list_dictionary(list1,list2):
    return [{list1[i]: list2[i]} for i in range(len(list1))]

colors = ["Black", "Red", "Maroon", "Yellow"]
color_codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]
print(list_dictionary(colors,color_codes))



# # 6. Write a Python program to check whether all dictionaries in a list are empty or not
empty_dict = [{},{},{}]
if empty_dict == []:
   print("The dictionary is empty")
else:
   print("The dictionary is not empty")


# # 7. Given a list of numbers, use list comprehension to remove all odd numbers from the list:
numbers = [3,5,45,97,32,22,10,19,39,43]
even_numbers = [num for num in numbers if num % 2 ==0]
print(even_numbers)


# # 8. Find the common numbers in two lists (without using a tuple or set)
list_1 = 1, 2, 3, 4,
list_2 = 2, 3, 4, 5
common_numbers = [a for a in list_2]
print(common_numbers)


# # 9. Use a nested list comprehension to find all of the numbers from 1-1000
# # that are divisible by any single digit besides 1 (2-9)
divisible_nummbers = [num for num in range(1, 1001) 
                      if any(num % i == 0 for i in range(2, 10))]
print(divisible_nummbers)


# # Write a Python function to remove all vowels in a string

def remove_vowels(string):
    vowels = "aeiouAEIOU"
    new_string = ""
    for char in string:
        if char not in vowels:
            new_string += char
    return new_string
print(remove_vowels("hello"))





          
        
