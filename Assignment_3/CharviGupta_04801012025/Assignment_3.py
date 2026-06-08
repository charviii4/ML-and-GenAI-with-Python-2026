# Assignment 3 (Internship)

# Print first 10 natural numbers
def nat_num():
    for i in range(1, 11):
        print(i)
nat_num()

# Calculate sum of first N natural numbers
def sum_num(n):
    return sum(range(1, n + 1))
n = int(input("Enter N: "))
print("Sum = ", sum_num(n))

# Reverse a number
def rev_num(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return rev
num = int(input("Enter Number: "))
print("Reversed Number = ", rev_num(num))

# Count Digits in a Number
def counter(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count
num = int(input("Enter Number: "))
print("Number of Digits = ", counter(num))

# Check Palindrome Number
def palindrome(num):
    og = num
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10

    if og == rev:
        print("Palindrome number")
    else:
        print("Not a palindrome number")
num = int(input("Enter Number: "))
palindrome(num)

# Generate Fibonacci Series
def fibonacci(n):
    a, b = 0, 1
  for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
n = int(input("\nEnter Number of Terms: "))
fibonacci(n)

# Calculator Using Functions
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
print("\n1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice = int(input("Enter your choice: "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice == 1:
    print("Result = ", add(num1, num2))
elif choice == 2:
    print("Result = ", subtract(num1, num2))
elif choice == 3:
    print("Result = ", multiply(num1, num2))
elif choice == 4:
    print("Result = ", divide(num1, num2))
else:
    print("Invalid Choice")

# Create a Text File and Store Student Details
file = open("student.txt", "w")
name = input("Enter Student Name: ")
marks = input("Enter Marks: ")
file.write("Name: " + name + "\n")
file.write("Marks: " + marks)
file.close()
print("Student Details Saved")

# Read Data from a File
file = open("student.txt", "r")
data = file.read()
print(data)
file.close()

# Handle Division by Zero Using Exception Handling
try:
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
  result = a / b
    print("Result =", result)
except ZeroDivisionError:
    print("Cannot Divide by Zero")

# Create a Student Class with Name and Marks
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
name = input("Enter Student Name: ")
marks = float(input("Enter Marks: "))
s1 = Student(name, marks)
s1.display()
