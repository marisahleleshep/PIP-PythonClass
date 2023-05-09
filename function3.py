# Write a Python program that takes a list of strings as input and outputs the number of times 
# each string appears in the list, using a dictionary and conditional statements.

def count_occurrence(str):
    occurrence_dict = {}
    for string in str:
        if string in occurrence_dict:
            occurrence_dict[string] += 1
        else:
            occurrence_dict[string] = 1
    return occurrence_dict

str = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
occurrence_dict = count_occurrence(str)
print(occurrence_dict)


# Write a Python program that takes a list of numbers as input and outputs the median of the numbers 

def calculatiton(numbers):
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    if length % 2 == 0:
        middle = length // 2
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
    else:
        middle = length // 2
        return sorted_numbers[middle]

# Write a Python program that takes a list of numbers as input and outputs 
# the second largest number in the list using conditional statements and a for loop.

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

largest = numbers[0]
second_largest = numbers[0]

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num

    elif num > second_largest:
        second_largest = num

print(second_largest)


# Write a Python program that takes a year as input and determines if it is a leap year.

year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is a leap year")
else:
    print(year, "is not a leap year")




# Write a Python program that takes a string as input and checks if it is a palindrome 
# (reads the same forwards and backwards), ignoring spaces and punctuation.
def is_palindrome(s):
    return s == s[::-1]
s = "dad"
if is_palindrome(s):
    print(s, "is a palindrome")
else:
    print(s, "is not a palindrome")

