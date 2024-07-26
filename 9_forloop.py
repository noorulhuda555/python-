# the for loop is a count controlled loop
# syntax as follows 
# for variable in [val1, val2, etc.]
      #statements 

#using a list 
print('printing numbers from 1 - 5 ')
for num in [1, 2, 3, 4, 5]:
    print(num)

# num assigned value 1 then print 
# num assigned value 2 then print 
# upto so on...

print('printing names')
for names in ['noor', 'sara', 'bob', 'david']:
    print(names)

#using range function
#print something n times 

for numbers in range(5):
    print(numbers)

for message in range (3):
    print('stupid baka')

#using range function to print from lower limit 
# to upper limit 
# print 1,2,3,4 not 5 
for n in range(1, 5):
    print(n)

#using range function to alter step value 
print('odd numbrs are :-')
for m  in range(1, 10, 2):
    print(m)

print('numbers\tsquares')
print('----------------')

for n in range(1, 11):
    print(n, '\t', n*n)

#reverse printling
for number in range(10, 5, -1):
    print(number)

big = 5
sum=0
for counter in range(big):
    chicken = int(input('enter a number'))
    sum+=chicken 

print('sum is finaaly found after so long i.e ',sum)    


