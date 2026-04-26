# A function is a block of code that performs a task.
def greet():
    print("Hello Sujal")

greet()


# A function can also take parameters.
def greet(name):
    print("Hello",name)

greet("Sujal")
greet("Rahul")



# A function can also return a value.   
def greet(name="Guest"):
 print("Hello",name)

greet()
greet("Sujal")


# Built-in functions in Python
# print()
# len()
# max()
# min()
# sum()



# Recursion is a technique where a function calls itself.
def count(n):
    if n==0:
       return
    print(n)
    count(n-1)

count(5)  # Output:- 5 4 3 2 1


# Factorial of a number using recursion
def fact(n):
    f=1
    for i in range(1,n+1):
       f*=i
    return f
print(fact(5))



# Function calling another function
def add(a,b):
 return a+b

def square(n):
 return n*n

x=add(2,3)
print(square(x))


# Create menu driven function program:
# Add  # Factorial   # Prime Check

def add(a,b):
    return a+b

def factorial(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f


def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True



print("1 Add")
print("2 Factorial")
print("3 Prime Check")

choice=int(input())

if choice==1:
    a=int(input())
    b=int(input())
    print(add(a,b))

elif choice==2:
    n=int(input())
    print(factorial(n))

elif choice==3:
    n=int(input())
    if prime(n):
        print("Prime")

else:
    print("Not Prime")



# 1 Find square of number
# 2 Check palindrome
# 3 Find sum of digits
def square(n):
    return n*n


def palindrome(n):
    temp=n
    rev=0

    while n>0:
        d=n%10
        rev=rev*10+d
        n=n//10
    return temp==rev

def digit_sum(n):
    s=0
    while n>0:
        s+=n%10
        n=n//10
    return s

n=int(input())
print(square(n))
print(palindrome(n))
print(digit_sum(n))    


