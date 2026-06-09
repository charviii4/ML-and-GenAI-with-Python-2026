#Assignment 1 (Internship)
#1 Area of a rectangle
l=int(input("Enter length of the rectangle:"))
b=int(input("Enter breadth of the rectangle:"))
area=l*b
print("Area of the rectangle=",area)

#2 Simple interest
principal=float(input("Enter the principal amount:"))
rate=float(input("Enter the rate in percentage:"))
time=float(input("Enter the time in years:"))
simple_interest=(principal*rate*time)/100
print("simple interest is : ", simple_interest)


#3 Temperature from celsius to fahrenheit
celsius=float(input("Enter the temperature in celsius:"))
fah=(celsius*9/5)+32
print(f"Temperature in fahrenheit is : {fah}")


#4 Average of three numbers
num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))
num3=float(input("Enter the third number:"))
average=(num1+num2+num3)/3
print("Required average: ", average)

#5 Square and cube of a number
num=float(input("Enter the number:"))
square=num**2
cube=num**3
print(f"Square: {square}, Cube: {cube}")

#6 Swap two numbers without third variable
a=int(input("Enter the first number (a):"))
b=int(input("Enter the second number(b):"))
print(f"Before swap: a={a},b={b}")
a,b=b,a
print(f"After swap: a={a},b={b}")

#7 Student report programme
#taking student details using input()
name=input("Enter the name:")
age=input("Enter the age:")
studentclass=input("Enter the class:")
#taking and storing marks in variables
cs_marks=float(input("Enter your cs marks:"))
maths_marks=float(input("Enter your maths marks:"))
english_marks=float(input("Enter your english marks:"))
chem_marks=float(input("Enter chemistry marks:"))
#calculating total and percentage
total=cs_marks+maths_marks+english_marks+chem_marks
percentage= (total / 400)*100
print("Total Marks= ",total)
print("Percentage= ",percentage )
