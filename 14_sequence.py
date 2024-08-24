"""list is a type of sequence
hold multiple items of data, contigous
2 types = list, tuple

"""

"""
lists 
multiple data items, mutable, dynamic,cam store diff data types
0 based indexing
-1 is last index, -2 is second last and so on
"""

data = ['alicia', '27', '155.6']
print(data)
numbers=list(range(1,10, 2))
print(numbers)
#reptition operator (*)   sequence * n
n=[0] * 5
print(n)
print(data[-1]) #last index

#concatenating using + operator 
list1 = [1,2,3,4]
list2 = [5,6,7,8]
list3 = list1+list2
print(list3)

#ppned using +=
list1 += list2
print(list1)

#list slicing select a specific range of items 
#list_name[start : end ]

midlist = list1[1:3]
print(midlist)
print(list1[1:])
print(list1[0:3:2]) #step value

"""
tuples 
basic diff from list is that it hs round brackets
immutable no append, remove, sort"""