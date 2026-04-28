# DAY 7 : STRINGS IN PYTHON
# 1. String Basics

name = "Sujal"
print(name)

a = "Hello"
b = 'Hello'
c = """Hello"""

print(a,b,c)

# 2. Indexing
s="Python"

print(s[0])
print(s[2])
print(s[-1])

# 3. Slicing
print(s[0:3])
print(s[2:5])
print(s[:4])
print(s[1:])
print(s[::2])
print(s[::-1])


# 4. String Operations
a="Hello"
b="World"

print(a+b)

print("Hi"*3)

print("Py" in "Python")


# 5. String Functions
print(len("Python"))
s="python"
print(s.upper())
print(s.lower())

s=" hello "
print(s.strip())

s="I like Java"
print(s.replace("Java","Python"))

s="I love coding"
print(s.split())

s="banana"
print(s.count("a"))


# 6. Loop Through String
s="Python"
for ch in s:
    print(ch)


# 7. Palindrome Check
word="madam"

if word==word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


#----------------- Practice Problems-----------------

# Count vowels

text="Programming"

count=0

for ch in text:
    if ch in "aeiouAEIOU":
        count+=1

print("Vowels =",count)


# Remove spaces

sentence="I love python"

print(sentence.replace(" ",""))


# Word Count

line="I love coding"

words=line.split()

print("Words =",len(words))


# Character frequency

text="banana"

print("Count of a =",text.count("a"))


# Anagram Check
a="listen"
b="silent"

if sorted(a)==sorted(b):
    print("Anagram")
else:
    print("Not Anagram")


# Mini Project
# Password Checker

password="mypassword123"

if len(password)>=8:
    print("Strong Password")
else:
    print("Weak Password")


# FINAL CHALLENGE
s="madam"

# Reverse
print("Reverse =",s[::-1])


# Vowel count
count=0

for ch in s:
    if ch in "aeiouAEIOU":
        count+=1

print("Vowels =",count)


# Palindrome
if s==s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# Uppercase
print(s.upper())

# BONUS PROBLEMS

# 1 Check if string contains digit

s="Python123"

has_digit=False

for ch in s:
    if ch.isdigit():
        has_digit=True

print("Contains digit:",has_digit)



# 2 Count consonants

s="Programming"

count=0

for ch in s:
    if ch.isalpha() and ch not in "aeiouAEIOU":
        count+=1

print("Consonants =",count)



# 3 Largest word in sentence

sentence="Python is amazing programming language"

words=sentence.split()

largest=max(words,key=len)

print("Largest word:",largest)
