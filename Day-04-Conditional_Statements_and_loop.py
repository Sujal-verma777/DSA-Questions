# Conditional Statements and Loop

marks = int(input())
if marks >= 90:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")


# Nested if
age = 22
citizen = True

if age >= 18:
    if citizen:
        print("Can vote")


# Short-hand if
a=10
b=20

print("A Greater") if a>b else print("B Greater")  


# Find the largest of three numbers
a=int(input())
b=int(input())
c=int(input())

if a>b and a>c:
 print(a)
elif b>c:
 print(b)
else:
 print(c)


# Simple Calculator
a=int(input())
op=input()
b=int(input())

if op=="+":
 print(a+b)
elif op=="-":
 print(a-b)
elif op=="*":
 print(a*b)
elif op=="/":
 print(a/b)


#------------------------------------------

range(5)       #0-4
range(1,6)     #1-5
range(1,10,2)  #odd numbers

# Sum of first n natural numbers
n=int(input())
sum=0
for i in range(1,n+1):
 sum+=i

print(sum)


# Print multiplication table of a number
n=int(input())
for i in range(1,11):
 print(n,"x",i,"=",n*i)



# Factorial of a number
n=int(input())
fact=1
for i in range(1,n+1):
 fact*=i
print(fact)


