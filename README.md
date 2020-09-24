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

extract a string from a larger strgin given indexes into the string

```python
s = 'hello'
s[0:4]  # 'hell'
#  s[i:j] -> i = beginning/inclusive, j = end/exclusive
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

Merge Sort (first recursion)

```python

def merge_sort(self, list):
    pass

    # 1. return if at the bottom    

    if len(list) <= 1:
        return list

    # 2. Break it down and save the one piece we want here
    #    -- determine if len is even or odd, set 'extra' to 0 (even) or 1 (odd)
    #    -- break at len(list)//2 (which returns an integer at the floor) 
    extra = len(list) % 2
    

    #    -- note: len(list) == len(list)//2 + len(list)//2 + extra (where extra is 1 if odd and 0 id even)
    #    --       for example:  5 = 5//2 + 5//2 + 1 , or 4 == 4//2 + 4//2 + 0
    #    --       so left_size = len(list)//2, right_size = len(list)//2 + extra
    #    --       and left = list[:left_size], right = list[right_size:]  # colon's go on left for left and right for right
    #    --       then recurse: left = merge_sort(left), and right=merge_sort(right)

    # 3. Finally, call merge
    #   -- result = merge(left, right)
    #   -- return result

    # To merge, combine the sorted left and right arrays to larger ones
    




```
