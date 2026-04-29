#----------Tuples---------- 
# A tuple is an ordered collection of elements that is immutable (cannot be changed after creation).
# Tuples are defined using parentheses () or the tuple() constructor

t=(10,20,30)
print(t)
# output: (10, 20, 30)

# Difference:----
# List mutable
# Tuple immutable
# Set mutable


t=(5,10,15)
print(t[0])
print(t[-1])
# output: 5
# output: 15    


# Tuple slicing
t=(1,2,3,4,5)
print(t[1:4])
print(t[::-1])
# output: (2, 3, 4)
# output: (5, 4, 3, 2, 1)   


# Tuples are immutable-----------
t=(1,2,3)
t[1]=99 
# output: TypeError: 'tuple' object does not support item assignment


# Tuple packing and unpacking----------
t=1,2,3
print(t)
# output: (1, 2, 3)

a,b,c=(10,20,30)
print(a)
print(b)
print(c)
# output: 10
# output: 20
# output: 30


# Tuple Methods------------------------
t=(1,2,2,2)
print(t.count(2))
# output: 3
print(t.index(2))
# output: 1
t=(5,2,9)
print(len(t))
# output: 3
print(max(t))
# output: 9
print(min(t))
# output: 2
print(sum(t))
# output: 16




#--------Sets----------
# Set is a collection of unique elements
# Sets are unordered and mutable
# Sets are defined using curly braces {} or the set() constructor

s={1,2,3}
print(s)
# output: {1, 2, 3}

s={1,2,2,3,3}
print(s)
# output: {1, 2, 3}  # Duplicates are removed

a=[1,2,2,3]
s=set(a)
print(s)
# output: {1, 2, 3}  # Duplicates are removed

s={1,2}
s.add(3)
print(s)
# output: {1, 2, 3}

s={1,2,3}
s.append(4)
# output: AttributeError: 'set' object has no attribute 'append'

s={1,2,3}
s.remove(2)
print(s)
# output: {1, 3}

s={1,2}
s.discard(5)
print(s)
# output: {1, 2}

s={1,2,3}
s.pop()
print(s)
# output: {2, 3}  # Removes random item. because sets are unordered, we cannot predict which item will be removed.

a={1,2,3}
b={3,4,5}
print(a|b)
# output: {1, 2, 3, 4, 5}  # Union of sets

print(a.union(b))
# output: {1, 2, 3, 4, 5}  # Union of sets

print(a&b)
# output: {3}  # Intersection of sets

print(a.intersection(b))
# output: {3}  # Intersection of sets

print(a-b)
# output: {1, 2}  # Difference of sets 

print(a^b)
# output: {1, 2, 4, 5}  # Symmetric difference of sets (elements in either a or b but not in both)

s={5,7,9}
print(7 in s)
# output: True

print(10 in s)
# output: False

