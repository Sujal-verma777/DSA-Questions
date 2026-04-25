# Fibonacci Series
n=int(input())

a=0
b=1

for i in range(n):
 print(a,end=" ")
 c=a+b
 a=b
 b=c



# Factorial of a number
n=int(input())

fact=1

for i in range(1,n+1):
 fact*=i

print(fact)



# Sum of digits of a number
n=int(input())
sum=0
while n>0:
 digit=n%10
 sum+=digit
 n=n//10

print(sum)




