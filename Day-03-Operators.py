# a = 10
# b = 3

# print(a + b)   # 13
# print(a - b)   # 7
# print(a * b)   # 30
# print(a / b)   # 3.33 (float)
# print(a // b)  # 3 (floor division)
# print(a % b)   # 1 (remainder)
# print(a ** b)  # 1000 (power)


# -----Check if a number is even or odd
# n = int(input())

# if n % 2 == 0:
#     print("Even")
# else:
#     print("Odd")



# -----Check if a number is positive, negative or zero
# if n > 0:
#     print("Positive")
# elif n < 0:
#     print("Negative")
# else:
#     print("Zero")    


# -----Check if a person is eligible to vote (age >= 18)
# age = int(input())
# if age >= 18 and age <= 60:
#     print("Eligible")
# else:
#     print("Not Eligible")   



# -----Check if a year is a leap year
# year = int(input()) 
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap Year") 
# else:
#     print("Not a Leap Year")



# -----Check if a number is positive even, positive odd, negative or zero
num = int(input())

if num % 2 == 0 and num > 0:
    print("Positive Even")
elif num % 2 != 0 and num > 0:
    print("Positive Odd")
elif num < 0:
#     print("Negative Number")
# else:
#     print("Zero")
