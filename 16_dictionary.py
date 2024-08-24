"""" stores collection of data 
a pair of key and value 
process is similar to real life dictionary
mappings(n)=keyy value pair bcz each key is mapped to a value

syntax :
dictionary_name={ 'key' : 'value', 'second key' : 'value'}
(comma separated)
string comparisons are case sensitive
"""
phonebook={'noor' : '000-111', 'sara' : '111-234', 'zara' : '111-234'}
print(phonebook['noor'])
#dictionary_name[key]

#can use in and not in methods 
if 'noor' in phonebook:
    print('noor found in phonebook')

if 'blob' not in phonebook:
    print('hehe no blob')

#adding new elements 
#dictionary_name[key]=value

print('before adding maria')
print(phonebook)
phonebook['maria']='555-555'
print('after adding maria ')
print(phonebook)
print('removing maria')
del phonebook['maria'] 
print(phonebook)
#del phonebook['maria'] dobara delete krne par key error ata hai 

#getting number of elements 

num_items=len(phonebook)
print('size of phone book', num_items)

print('a funny looking dictionary')
mixed = {'abc' : 1, 99 : 'yada', (3,4,4) : [1,2,3]}
print(mixed)


#iterate over a dictionary
for key in phonebook:
    print(key, phonebook[key])
    #phonebook[key] gives value 

#methods
#dictionary.get(key, default)
getvalue=phonebook.get('zara', 'not found')
print(getvalue)

print(phonebook.items())

for key in phonebook.items():
    print(key)

#dictionary.pop(key, default)

removeditem = phonebook.pop('sara', 'not found')
print(removeditem)
removeditem = phonebook.pop('sara', 'not found')
print(removeditem) #secnd time its not found bcz removes 

randomlyremoved=phonebook.popitem()
print('randomly')
print(randomlyremoved)

for val in phonebook.values():
    print(val)