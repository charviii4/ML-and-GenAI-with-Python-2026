#Assignment 2 (Internship)

# Sum of first ten natural numbers
total=sum(range(1,11))
print(f"Sum of first ten natural numbers is: {total}")

# Factorial of a number
num=int(input("Enter number:"))
factorial=1
if num<0:
    print("Factorial does not exist")
elif num==0:
    print("Factorial of 0 is 1.")
else:
    for i in range(1,n+1):
        factorial=factorial*i
    print(f"Factorial of {num} is {factorial}")

# Fibonacci Series
a,b=0,1
n=int(input("Enter number greater than 1 for series:"))
series=[]
for i in range(1,n+1):
    series.append(a)
    a,b=b,a+b
print(series)

# Largest among three numbers
a=float(input("Enter first number:"))
b=float(input("Enter second number:"))
c=float(input("Enter third number:"))
if a>b and a>c:
    largest=a
elif b>a and b>c:
    largest=b
else:
    largest=c
print("Largest number:",largest)

# Student result system
name=input("Enter name:")
age=input("Enter age:")
grade=input("Enter class:")

cs_marks=float(input("Enter cs marks:"))
beee_marks=float(input("Enter beee marks:"))
phy_marks=float(input("Enter physics marks:"))
chem_marks=float(input("Enter chemistry marks:"))

total=cs_marks+beee_marks+phy_marks+chem_marks
percentage=total/5
print("Percentage=",percentage)

if p>=93:
    grade="A+"
elif p>=85 and p<93:
    grade="A"
elif p>=77 and p<85:
    grade="B+"
elif p>=69 and p<77:
    grade="B"
elif p>=61 and p<69:
    grade="C"
elif p>=53 and p<61:
    grade="D"
else:
    grade="F"
print("Grade=",grade)
