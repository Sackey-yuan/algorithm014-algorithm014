'''collections
This module implements specialized container datatypes providing
alternatives to Python's general purpose built-in containers, dict,
list, set, and tuple.

* namedtuple   factory function for creating tuple subclasses with named fields
* deque        list-like container with fast appends and pops on either end
* ChainMap     dict-like class for creating a single view of multiple mappings
* Counter      dict subclass for counting hashable objects
* OrderedDict  dict subclass that remembers the order entries were added
* defaultdict  dict subclass that calls a factory function to supply missing values
* UserDict     wrapper around dictionary objects for easier dict subclassing
* UserList     wrapper around list objects for easier list subclassing
* UserString   wrapper around string objects for easier string subclassing

'''
from collections import deque

def mydeque():
    d  = deque('1234556')
    print(d) #deque(['1', '2', '3', '4', '5', '5', '6'])
    d.appendleft('a')
    d.append('b')
    print(d) #deque(['a', '1', '2', '3', '4', '5', '5', '6', 'b'])
    # print(d.popleft())
    # #b
    # print(d.pop())
    # #6
    # print(d.pop())
    # #a
    c = d.copy()
    print(d.count('2'))
    d.extend('123')
    d.extendleft('32523')
    print(d.index('2'))
    # d.clear()
    d.remove('3')
    d.reverse()
    d.remove('1')
    print(d)
    d.rotate(3)#Rotate the deque n steps to the right (default n=1).  If n is negative, rotates left.
    print(d)

# hash_map = {1:1}
ls = [["8"]*4]*4
lb = [["8"]*4 for _ in range(4)]
ls[1][1] = 's'
lb[1][1] = 's'
print('ls\n',ls)
print('lb\n',lb)
