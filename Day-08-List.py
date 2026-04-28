numbers = [10,20,30,40]
print(numbers)
# output: [10, 20, 30, 40]


data=[10,"Python",3.14,True]
print(data)
# output: [10, 'Python', 3.14, True]


# List indexing
a=[5,10,15,20]
print(a[0])
print(a[2])
print(a[-1])
# output: 5
# output: 15
# output: 20


# List slicing
a=[1,2,3,4,5]
print(a[1:4])
print(a[:3])
print(a[::2])
# output: [2, 3, 4]
# output: [1, 2, 3]
# output: [1, 3, 5]


# Adding Elements
a=[1,2]
a.append(2)
print(a)
# output: [1, 2, 2]

a=[1,2]
a.append(3)
print(a)
# output: [1, 2, 3]


a=[1,3]
a.insert(1,2)
print(a)
# output: [1, 2, 3]


a=[1,2]
a.extend([3,4])
print(a)
# output: [1, 2, 3, 4]

a=[1,2]
a.extend([2,3])
print(a)
# output: [1, 2, 2, 3]


a=[1,2,3]
a.remove(2)
print(a)
# output: [1, 3]


a=[10,20,30]
a.pop()
print(a)
# output: [10, 20]


a=[1,2,3]
del a[1]
print(a)
# output: [1, 3]


a=[1,2,3]
print(len(a))
# output: 3


a=[10,20,30]
print(sum(a))
# output: 60


a=[7,2,9]
print(max(a))
print(min(a))
# output: 9
# output: 2


a=[4,1,8,2]
a.sort()
print(a)
# output: [1, 2, 4, 8]


a=[4,1,8,2]
a.sort(reverse=True)
print(a)
# output: [8, 4, 2, 1]


a=[1,2,3]
a.reverse()
print(a)
# output: [3, 2, 1]


a=[10,20,30]
for i in a:
    print(i)
# output: 10
# output: 20
# output: 30


a=[10,20,30]
for i in range(len(a)):
    print(a[i])
# output: 10
# output: 20
# output: 30


# Linear Search
a=[5,9,2,7]
key=2
if key in a:
    print("Found")
# output: Found


# Linear Search using loop (Manual)
a=[5,9,2,7]
key=7
for i in a:
    if i==key:
        print("Found")
# output: Found



# -------------question----------------

# 1. Sum all elements.
a=[5,10,15]
total=0
for i in a:
    total+=i
print(total)
# output: 30

# 2. Find the largest element.
a=[7,11,3]
largest=a[0]
for i in a:
    if i>largest:
        largest=i
print(largest)
# output: 11

# 3. Reverse without reverse()
a=[1,2,3]
print(a[::-1])
# output: [3, 2, 1]

# 4. find output.
a=[10,30,20,50]
a.sort()
print(a[-2])
# output: 30

# 5. Take a list and do:
# 1 Sum
# 2 Largest
# 3 Smallest
# 4 Sort
# 5 Reverse

a=[8,3,15,2,9]
print("Sum =",sum(a))
print("Largest =",max(a))
print("Smallest =",min(a))
a.sort()
print("Sorted =",a)
print("Reverse =",a[::-1])
# output:-
# Sum = 37
# Largest = 15
# Smallest = 2
# Sorted = [2, 3, 8, 9, 15]
# Reverse = [15, 9, 8, 3, 2]
