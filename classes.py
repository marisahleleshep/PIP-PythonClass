# Define a class Rectangle with attributes width and height, and methods area() and perimeter().
# Define a subclass Square that inherits from the Rectangle class and has an additional size attribute.
# Override the area() and perimeter() methods to work with the size attribute instead of width and height.
# 5:29


class Rectangle: 
    def __init__( self, width, height):
        self.width=width
        self.height=height

    def area (self):
        return self.width *self. height
    
    def perimeter(self):
        return (self. width + self. height)*2
    def identity(self):
        return f"The width {self. width} and height {self.height}"

rectangle1=Rectangle(240,200)
print(rectangle1.area())
print(rectangle1.perimeter())
print(rectangle1.identity())

class Square(Rectangle):
    def __init__(self,size):
        self.size=size
        super().__init__(size,size)
    def area(self):
        return self.size**2
    def perimeter(self):
        return self.size*4
    
square1=Square(100)
print(square1.area())
print(square1.perimeter())

    



# Define a class BankAccount with attributes balance and owner_name, and methods deposit() and withdraw() that modify the balance attribute.
class BankAccount:
    def __init__(self,balance,owner_name):
        self.balance=balance
        self.owner_name=owner_name

    def deposit(self,amount):
        self. balance+=amount
    def withdraw(self,amount):
        self. balance<=amount

bankAccount=BankAccount(45000,"John")
print(bankAccount.deposit())
print(bankAccount.withdraw())



# Define a class Person with attributes name and age, and a method greet() that prints "Hello, my name is [name] and I am [age] years old.".
#  Define a subclass Student that inherits from the Person class and has an additional attribute student_id. Override the greet() method to print "Hello, my name is [name], I am [age] years old, and my student ID is [student_id]." instead.

# Define a class Bank that has a dictionary attribute accounts that maps account IDs (integers) to BankAccount objects.
#  Implement methods create_account() that creates a new BankAccount object with a unique account ID and adds it to the accounts dictionary,
# and get_account() that retrieves a BankAccount object from the accounts dictionary by ID.


