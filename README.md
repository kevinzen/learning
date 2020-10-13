# Code Learning Notes 

This file contains notes on the python language for common problems.

### Working with Lists (arrays):

To iterate the langth of a List:

```python
# given array 'arr'
arr = [1,2,3,4]
for index in range(len(arr)):
    print(index)
```

Python ranges used for iterating with for loops:

```python
r = range(6) 
for n in r:
    print(n)
```

Indexing lists and dictionaries (arrays and hashes):

```python

# if indexes are generally sequential, use an array
# since you can iterate using `for index in range(len(array)):`

array = [1,2,3,4,5]
for index in range(len(array)):
    print(index)

# if indexes are random, use a dictionary. Iterate with `for each   

dict = {'a':1, 'b':2, 'c':3 }
for key in dict:
    print(key) 

# to get both the key and value
for key, value in dict.items():
    print key, value


``` 

When retriving a value from a dictionary, always use `.get()` rather than subscripting it

```python
# NO!
a = {}
a[2]     # ==> Key Error! 
a.get(2) # YES!
```


When fetching a value from a dictionary or list, make sure to use the correct accessors.

```python

# Always subscript a List (array) 
a = [1,2,3]
a[0] == 1            

# Always .get from a Dictionary (Hash) 
b =  {'a':1, 'b':2, 'c':3 }
a.get('a') == 1 

```

To enumerate / iterate over a string in Python


```python

string_val = 'i am a string'

for element in string_val:
    print(element)

# or, to enumerate and get an index to the string

for i, v in enumerate(string_val):
    print(i,v)

```

# misc string operations

```python
# extract a string from a larger strgin given indexes into the string
s = 'hello'
s[0:4]  # 'hell'
#  s[i:j] -> i = beginning/inclusive, j = end/exclusive

# split a sentence into a list of words
text = "I am a sentence"
words = text.split() # words = ["I", "am", "a", "sentence"]

# count of occurrances of a letter
spaces = text.count(' ')  # 3 spaces

# create a senence from an array of words
new_sentence = (" ").join(words) 

# create a new string initialized with a number of specific chars

a_hundred_spaces = " " * 100

```

To reverse a list or a string

```python
a = [0,1,2,3]
b = a[::-1]
# now b = [3,2,1,0]

```

Partitioning arrays in general

```python
a = [0,1,2,3,4,5]
a[0]     # = 0
a[1]     # = 1
a[2:3]   # = 2 -> only returns one
         # in general, a[n:m] returns m-n elements, assuming m-n is positive and neither m nor n are out of range
a[2,2]   # = [] --> m - n = 0 elements returned
a[2:]    # = [2,3,4,5] -> from index 2 to the end. 
         # in general, a[m:] returns len(a) - m elements (in this case 6-2)
a[:2]    # = [0,1]
         # in general, a[:m] returns m elements beginning with 0 
         # and in general, a[start:end] returns end-start elements. 
         # from the 'start' index to the 'end' index, but not including the 'end' index 

         # finding the 'middle index' to break a list in half
a = [0,1,2,3,4]
mid_index = len(a) // 2 + len(a) % 2  #  mid_index = 3 and left = [0,1,2] and right = [3,4]
left = a[:mid_index]
right = a[mid_index:]

a = [0,1,2,3,4,5]
mid_index = len(a) // 2 + len(a) % 2  #  mid_index = 3 and left = [0,1,2] and right = [3,4,5]

a = [0]
mid_index = len(a) // 2 + len(a) % 2  #  mid_index = 1 and left = [0,1,2] and right = [3,4,5]

         # 'consuming' elements out of an array

a = [0,1,2,3,4,5]
a.pop(0)           # returns '0', leaving a = [1,2,3,4,5]
a.pop(0)           # returns '1', leaving a = [2,3,4,5]
a.pop(0)           # returns '2', leaving a = [3,4,5]

a = [0,1,2,3,4,5]
a.pop(len(a)-1)    # returns '5', leaving a = [0,1,2,3,4]
a.pop(len(a)-1)    # returns '4', leaving a = [0,1,2,3]
a.pop(len(a)-1)    # returns '3', leaving a = [0,1,2]

                    # appending elements in a list (add at end)
a = []
a.append(0)         # a = [0]
a.append(1)         # a = [0,1]
a.append(2)         # a = [0,1,2]
a.append(3)         # a = [0,1,2,3]

a = []
a.insert(0,3)         # a = [3]
a.insert(0,2)         # a = [2,3]
a.insert(0,1)         # a = [1,2,3]
a.insert(0,0)         # a = [0,1,2,3]


```


To convert a string to a list, and to pull substring from list

```python
a = 'i am a string'
b = list(a)         # b => ['i', 'a', 'm', ' ', 'a', ' ', 's', 't', 'r', 'i', 'n', 'g']

# note, it's better to just enumerate the string to iterate over its letters
for index,value in enumerate(a):
    print(index,value)
 
# substrings

a[0:1]
# returns string => 'i' 

b[0:1]
# returns list => ['i']

# reverse a string
a[::-1]
# returns 'gnirts a ma i'

# compare two strings
a = 'foo'
b = 'bar'
c = 'foo'

a == b # False
a == c # True

```

a `for` loop using a range() function

Note that the range() function doesn’t include the last (stop) number in the result.


```python
#  The signatures can be:

print("\nrange(stop)")
stop = 5
for i in range(stop):  # => 0,1,2,3,4
    print(i, end=', ')

stop = 5
start = 2
print("\nrange(start, stop)")
for i in range(start, stop):  # => 2,3,4
    print(i, end=', ')

start = 5-1
stop = -1
step = -1
print("\nrange(start, stop, step)")
for i in range(start, stop, step):  # => 4,3,2,1,0
    print(i, end=',')

# or, better said -> to walk a list backwards
print("\nrange(len(list)-1, -1, -1)")
for i in range(start, stop, step):  # => 4,3,2,1,0
    print(i, end=',')
  
# note:  range() function doesn’t include the last (stop) number in the result.
#        if counting down using a range, go down to -1
#        to count down an array: `for i in range(len(nums)-1, -1, -1)`
``` 

Insertion Sort:

```python

nums = [3,2,1,0]
nums_init = nums
for i in range(1, len(nums)): # 1, 2, 3
    for j in range(i-1, -1, -1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

# print(nums, nums_init)
# return nums

# running time complexity O(n^2)

```

Merge Sort

```python

def sort(self, list):
    # 1. return if at the bottom
    # 2. Divide
    # 3. Conquer

    # a list of zero or one is already sorted
    if len(list) <= 1:
        return list

    # if len = 11, then extra = 1, half = 5, left = list[:5], right = [6:]
    extra = len(list) % 2
    half_size = len(list) // 2
    mid_index = half_size + extra

    left = list[:mid_index]
    right = list[mid_index:]

    left = self.sort(left)
    right = self.sort(right)

    return self.merge(left, right)


def merge(self, left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result = result + left + right
    return result

```

sorted containers

```python
from sortedcontainers.sortedlist import SortedList
from sortedcontainers.sortedset import SortedSet

a = [1,2,3,3,2,1,1,2,3,4,6,9,8,8,8,6,5,5,9,8,5,4]

sl = SortedList(a)
# sl = [1,1,1,2,2,2,3,3,3,4,4,5,5,5,6,6,8,8,8,8,9,9]

# 'irange' generates iterator based on values stored in the list
s_range = list(sl.irange(4,6,(True, True)))  # (True,True) means inclusive of first and last numbers
# list(s_range) = [4, 4, 5, 5, 5, 6, 6] 

# 'islice' generates iterator based on index places in the list
s_slice = sl.islice(2,12)
# list(s_slice) = [1,2,2,2,3,3,3,4,4,5]

ss = SortedSet(a)
# ss = [1,2,3,4,5,6,8,9]

```

bisect used to break apart sorted lists == binary search for O(log(n))? speed for search. 

```python
from sortedcontainers.sortedlist import SortedList
from sortedcontainers.sortedset import SortedSet

a = [1,2,3,3,2,1,1,2,3,4,6,9,8,8,8,6,5,5,9,8,5,4]
sl = SortedList(a)

#     sl = [1,1,1,2,2,2,3,3,3,4,4,5,5,5,6,6,8,8,8,8,9,9]
# indexes: [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1] 

bl_index = sl.bisect_left(4)    # 9
br_index = sl.bisect_right(4)   # 11
# '4' is in the list, so BL != BR

bl_index = sl.bisect_left(99)   # 22
br_index = sl.bisect_right(99)  # 22
# 99 greater than any in the list, so BR == len(sl) and BL = len(sl)

bl_index = sl.bisect_left(0)   # 0
br_index = sl.bisect_right(0)  # 0
# 0 less than any in the list, so BR == 0 and BL = 0

bl_index = sl.bisect_left(7)   # 16
br_index = sl.bisect_right(7)  # 16
# 7 not in list, but list has both higher and lower values
# BL == BR. Both point to first value higher than 7

bl_index = sl.bisect_left(1)   # 0
br_index = sl.bisect_right(1)  # 3
# 1 is first in list. List contains value so BL != BR
# BL points to first occurence of value, BR points to index past last occurrance
# also, BR - BL = (number of '1's present in the sorted list)

```

Use lambdas as Anonymous Functions limited to one line

```python
a = ['cat','dog','bird']
for i in a:
    print(i) 

# prints:
# 'cat'
# 'dog'
# 'bird'

# use lambda to order indexes in order of the original List
b = [9, 22, 1, 4, 44]
l = len(b)

# c = list of indexes to elements in b sorted in ascending order b[i]
c = sorted(range(l), key=lambda i: b[i])
# c == [2, 3, 0, 1, 4]

# now we can print b in sorted, ascending order
for i in c:
    print(b[i]) 

d = c.copy()
# use lamdas to specify sort order for List elements
d.sort(key = lambda i: -b[i])
# d == [4, 1, 0, 3, 2]

# and we can print d in sorted, descending order
for i in d:
    print(b[i]) 

```

Generating lists using list comprehension and generators

```python

l = [x for x in range(10)]
# l == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

l = [x ** 2 for x in range(10) if x % 2 == 0]
# l == [0, 4, 16, 36, 64]

# initialize an array of treenode values:
node_vals = [2,1,3]
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Create a list of trees
forest = [TreeNode(x) for x in node_vals]

```

Build binary tree breadth first from an array of vals. 
Should be usable for any binary tree with only left and right subnodes

```python

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class TreeBuilder:
    def build_tree_breadth_first(self, node_vals: []):

        if len(node_vals) == 0:
            return []

        count = len(node_vals)
        nodes = {}

        RIGHT = 1
        LEFT = 2
        def build_tree(parent_node_index, node_index, r_or_l):

            if node_index >= count or node_vals[node_index] is None:
                return

            node_val = int(node_vals[node_index])
            nodes[node_index] = TreeNode(node_val)

            if r_or_l == LEFT:
                nodes[parent_node_index].left = nodes[node_index]
            else:
                nodes[parent_node_index].right = nodes[node_index]

            build_tree(node_index, 2*node_index+1, LEFT)
            build_tree(node_index, 2*node_index+2, RIGHT)

        # first, capture the tree head
        head_val = int(node_vals[0])
        nodes[0] = TreeNode(head_val)
        build_tree(0,1,LEFT)
        build_tree(0,2,RIGHT)

        return nodes[0]

```

Use `re.sub` instead of `str.replace` if you need regular expression matching

```python
import re
path = '/a/b/c/d/../.'
path = re.sub('/\.$', '', path)   # in case it's at the end

# path should now be: '/a/b/c/d/../d/e/' -> strip trailing '/' if there
path = re.sub('/$', '', path)   # in case it's at the end

```

To write a pytest test case

```python
import unittest
class SolutionTest(unittest.TestCase):
    def test_solution(self):
        pass
```

Sorting algorithm complexities



| algorithm |  BEST	|AVERAGE|WORST|
|-----------|-------|-------|-------|
| Selection Sort | Ω(n^2) | θ(n^2) | O(n^2) | 	 
| Bubble Sort | Ω(n) | θ(n^2) | O(n^2) | 	 
| Insertion Sort | Ω(n) | θ(n^2) | O(n^2)	  | 
| Heap Sort | Ω(n log(n)) | θ(n log(n)) | O(n log(n))	 |  
| Quick Sort | Ω(n log(n)) | θ(n log(n)) | O(n^2)	  | 
| Merge Sort | Ω(n log(n)) | θ(n log(n)) | O(n log(n))	 |  
| Bucket Sort | Ω(n+k) | θ(n+k) | O(n^2)	  | 
| Radix Sort | Ω(nk) | θ(nk) | O(nk)	  | 