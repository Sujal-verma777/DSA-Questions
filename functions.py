# Basic and Most Used Python Functions/Methods
# Organized by category. Each includes:
# - Comment explaining what it does
# - One example with output via print

# =============== STRING METHODS ===============
def string_examples():
    # str.split(): Splits string into list using separator
    text = 'hello world python'
    print('split():', text.split())  # ['hello', 'world', 'python']
    
    # str.join(): Joins list into string with separator
    words = ['hello', 'world']
    print('join():', ' '.join(words))  # hello world
    
    # str.strip(): Removes leading/trailing whitespace
    text = '  hello  '
    print('strip():', repr(text.strip()))  # 'hello'
    
    # str.replace(): Replaces occurrences of substring
    text = 'hello world'
    print('replace():', text.replace('world', 'python'))  # hello python
    
    # str.format(): Formats string with placeholders
    name = 'Python'
    print('format():', 'Hello, {}!'.format(name))  # Hello, Python!
    
    # str.upper()/lower(): Converts case
    text = 'Hello'
    print('upper():', text.upper())  # HELLO
    print('lower():', text.lower())  # hello
    
    # str.find(): Finds index of substring (returns -1 if not found)
    text = 'hello world'
    print('find():', text.find('world'))  # 6
    
    # str.startswith()/endswith(): Checks prefix/suffix
    text = 'hello.py'
    print('startswith():', text.startswith('hello'))  # True
    print('endswith():', text.endswith('.py'))  # True

# =============== LIST METHODS ===============
def list_examples():
    # list.append(): Adds item to end
    lst = [1, 2]
    lst.append(3)
    print('append():', lst)  # [1, 2, 3]
    
    # list.pop(): Removes/returns item at index (default last)
    lst = [1, 2, 3]
    item = lst.pop()
    print('pop():', item, lst)  # 3 [1, 2]
    
    # list.remove(): Removes first occurrence of value
    lst = [1, 2, 2]
    lst.remove(2)
    print('remove():', lst)  # [1, 2]
    
    # list.sort(): Sorts list in place
    lst = [3, 1, 2]
    lst.sort()
    print('sort():', lst)  # [1, 2, 3]
    
    # list.reverse(): Reverses list in place
    lst = [1, 2, 3]
    lst.reverse()
    print('reverse():', lst)  # [3, 2, 1]
    
    # list.extend(): Extends with another iterable
    lst = [1, 2]
    lst.extend([3, 4])
    print('extend():', lst)  # [1, 2, 3, 4]
    
    # list.index(): Returns index of first occurrence
    lst = [1, 2, 3]
    print('index():', lst.index(2))  # 1
    
    # list.count(): Counts occurrences
    lst = [1, 2, 2]
    print('count():', lst.count(2))  # 2

# =============== DICTIONARY METHODS ===============
def dict_examples():
    # dict.get(): Gets value with default if key missing
    d = {'a': 1}
    print('get():', d.get('b', 0))  # 0
    
    # dict.keys()/values()/items(): Views of keys/values/pairs
    d = {'a': 1, 'b': 2}
    print('keys():', list(d.keys()))  # ['a', 'b']
    print('values():', list(d.values()))  # [1, 2]
    print('items():', list(d.items()))  # [('a', 1), ('b', 2)]
    
    # dict.update(): Updates with another dict/iterable
    d = {'a': 1}
    d.update({'b': 2})
    print('update():', d)  # {'a': 1, 'b': 2}
    
    # dict.pop(): Removes/returns key value
    d = {'a': 1}
    val = d.pop('a')
    print('pop():', val, d)  # 1 {}
    
    # 'in' operator: Checks key existence
    d = {'a': 1}
    print('in:', 'a' in d)  # True

# =============== SET METHODS ===============
def set_examples():
    # set.add(): Adds element
    s = {1, 2}
    s.add(3)
    print('add():', s)  # {1, 2, 3}
    
    # set.remove(): Removes element (KeyError if missing)
    s = {1, 2, 3}
    s.remove(2)
    print('remove():', s)  # {1, 3}
    
    # set.union(): Union of sets
    s1 = {1, 2}
    s2 = {2, 3}
    print('union():', s1.union(s2))  # {1, 2, 3}
    
    # set.intersection(): Common elements
    print('intersection():', s1.intersection(s2))  # {2}
    
    # set.difference(): Elements in first not second
    print('difference():', s1.difference(s2))  # {1}

# =============== TUPLE & RANGE ===============
def tuple_range_examples():
    # tuple: Immutable list-like, use indexing
    t = (1, 2, 3)
    print('tuple index:', t[1])  # 2
    
    # range(): Generates sequence
    r = range(3)
    print('range():', list(r))  # [0, 1, 2]
    print('range step:', list(range(0, 10, 2)))  # [0, 2, 4, 6, 8]

# =============== FILE I/O ===============
def file_examples():
    # open() read/write
    with open('temp.txt', 'w') as f:
        f.write('hello')
    with open('temp.txt', 'r') as f:
        content = f.read()
    print('file read:', repr(content))  # 'hello'
    # Note: temp.txt created/deletable

# =============== MATH FUNCTIONS ===============
def math_examples():
    # abs(): Absolute value
    print('abs():', abs(-5))  # 5
    
    # round(): Rounds float
    print('round():', round(3.14159, 2))  # 3.14
    
    # min()/max(): Min/max of iterables
    nums = [1, 3, 2]
    print('min/max:', min(nums), max(nums))  # 1 3
    
    # pow(): Power (base**exp)
    print('pow():', pow(2, 3))  # 8
    
    # sum(): Sum of iterable
    print('sum():', sum([1, 2, 3]))  # 6

# =============== DATETIME ===============
def datetime_examples():
    from datetime import datetime
    # datetime.now(): Current date/time
    now = datetime.now()
    print('datetime:', now.strftime('%Y-%m-%d %H:%M'))  # e.g., 2024-01-01 12:00

# =============== JSON ===============
def json_examples():
    import json
    # json.dumps()/loads(): Serialize/deserialize
    data = {'key': 'value'}
    s = json.dumps(data)
    print('json dumps:', s)  # {"key": "value"}
    loaded = json.loads(s)
    print('json loads:', loaded['key'])  # value

# =============== OS/SYS ===============
def os_sys_examples():
    import os, sys
    # os.getcwd(): Current working directory
    print('cwd:', os.getcwd())
    
    # os.listdir(): List directory contents
    print('listdir top:', os.listdir('.')[:3])  # First 3 files
    
    # sys.argv: Command line args
    print('argv len:', len(sys.argv))  # Usually 1

# =============== ITERATORS & FUNCTIONAL ===============
def iterator_examples():
    # lambda: Anonymous function
    sq = lambda x: x**2
    print('lambda:', sq(3))  # 9
    
    # map(): Apply function to iterable
    nums = [1, 2, 3]
    print('map:', list(map(lambda x: x*2, nums)))  # [2, 4, 6]
    
    # filter(): Filter by predicate
    print('filter:', list(filter(lambda x: x > 1, nums)))  # [2, 3]
    
    # zip(): Pairs iterables
    print('zip:', list(zip(nums, ['a', 'b', 'c'])))  # [(1, 'a'), (2, 'b'), (3, 'c')]
    
    # enumerate(): Index + value
    print('enumerate:', list(enumerate(['a', 'b'])))  # [(0, 'a'), (1, 'b')]
    
    # any()/all(): Check conditions
    print('any:', any([False, True]))  # True
    print('all:', all([True, True]))  # True

# =============== RUN ALL EXAMPLES ===============
if __name__ == '__main__':
    print('=== Python Basic Functions Demo ===\\n')
    string_examples()
    print()
    list_examples()
    print()
    dict_examples()
    print()
    set_examples()
    print()
    tuple_range_examples()
    print()
    file_examples()
    print()
    math_examples()
    print()
    datetime_examples()
    print()
    json_examples()
    print()
    os_sys_examples()
    print()
    iterator_examples()
    print('\\n=== Demo Complete ===')
