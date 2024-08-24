""" works like maths wale sets 
all unique elements 
unordered, any data type
"""

#creating a set
emptyset = set()
fullset= set(['a', 'b', 'c']) #have to pass iterable value such as list, tuple or string
stringset=set(['stringsetcharcters']) #considered set of charcters 

#errorset= set('one', 'two', 'three') only one argumment can be passed

#get number of elements
len_fullset=len(fullset)
print(len_fullset)
print(len(emptyset))

#adding an element
fullset.add(1)
fullset.add(45)
print(fullset)

fullset.update([4,5,6])
print(fullset)


fullset.remove(1)
fullset.discard(45)
print(fullset)
#fullset.discard(1) # does not raise an error
#fullset.remove(1) #error 

for var in fullset:
    print(var)

#can use in or not in methods 

#union
set2 = set([12,13,14,'a'])
unionset = fullset.union(set2)


unionset = fullset | set2
print(unionset)

#intersection
intersectionset = fullset.intersection(set2)

interset= fullset & set2 
print(intersectionset)


#difference 
diffset = fullset.difference(set2)
print(diffset)
diffset= fullset - set2
print(diffset)

#symmetric difference = elemnts in one set or other but not in both
sdiffset = fullset.symmetric_difference(set2)
sdiffset= fullset ^ set2 
print(sdiffset)

set_1=set([1,2,3,4])
set_2 = set([2,3])
print(set_2.issubset(set_1))
print(set_2<=set_1) #subset
print(set_1.issuperset(set_2))
print(set_1 >= set_2) #superset
