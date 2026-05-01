# What is Dictionary?
# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.{key : value}

student = {
    "name": "Sujal",
    "age": 20,
    "course": "CSE"
}
print(student)
# output: {'name': 'Sujal', 'age': 20, 'course': 'CSE'}

# ----------Accessing Values----------
student = {"name":"Sujal","age":20}
print(student["name"])
print(student.get("age"))
print(student.get("course")) # This will return None because "course" key does not exist in the dictionary.
print(student["course"]) # This will raise an error because "course" key does not exist in the dictionary.

# output: Sujal
#         20
#         None


# ----------Adding and Updating Values----------
student = {"name":"Sujal"}
student["age"] = 20   # add
student["name"] = "Rahul"  # update
print(student)
# output: {'name': 'Rahul', 'age': 20}


# ----------Removing Values----------
student = {"name":"Sujal","age":20}
student.pop("age")
print(student)
# output: {'name': 'Sujal'}
student = {"name":"Sujal","age":20}
student.popitem()
print(student) 
# output: {'name': 'Sujal'}


# ----------Loop Through Dictionary----------
d={"a":1,"b":2}
for k in d:
    print(k) 
# output: a
#         b

for v in d.values():
    print(v)
# output: 1
#         2

for k,v in d.items():
    print(k,v)
# output: a 1
#         b 2    


# ----------Important Methods----------
d={"a":1,"b":2}
print(d.keys())
# output: dict_keys(['a', 'b'])

print(d.values())
# output: dict_values([1, 2])

print(d.items())
# output: dict_items([('a', 1), ('b', 2)])


d={"a":1}
print("a" in d)
# output: True

#----------Nested Dictionary----------
student = {
 "name":"Sujal",
 "marks":{
     "math":90,
     "phy":85
 }
}
print(student["marks"]["math"])
# output: 90


# ----------Practice----------
d={}
n=3

for i in range(n):
    key=input("Enter key: ")
    value=input("Enter value: ")
    d[key]=value
print(d)
# output: Enter key: name
#         Enter value: Sujal    
#         Enter key: age
#         Enter value: 20
#         Enter key: course
#         Enter value: CSE
#         {'name': 'Sujal', 'age': '20', 'course': 'CSE'}


# ----------Dictionary Comprehension----------
squares = {x:x*x for x in range(1,6)}
print(squares)
# output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}



#----------Task 1: Print all keys & values----------
d={"a":10,"b":20}
for k,v in d.items():
    print(k,v)
# output: a 10
#         b 20


# ----------Task 2: Count frequency-----------
a=[1,2,2,3,3,3]
freq={}
for i in a:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)
# output: {1: 1, 2: 2, 3: 3}


# ----------Task 3: First non-repeating element----------
a=[1,2,2,3,3]
freq={}
for i in a:
    freq[i]=freq.get(i,0)+1
for i in a:
    if freq[i]==1:
        print(i) 
        break
# output: 1


# ----------Task 4: Merge two dictionaries----------
d1={"a":1,"b":2}
d2={"c":3,"d":4}    
d1.update(d2)
print(d1)
# output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
