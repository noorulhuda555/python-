n1 = 2
n2 = 4
n3 = 2
#listed in order of highest to lowest precedence
print(n1 ** n2) #power right to left assocition
#all below have left ro right association
print(n1 * n2) #multiply 
print(n1 / n2 ) #divides and give float ans
print(n1 // n2) # division asnwer as int
print(n1 % n2) #remainder
print(n1 + n2) #add
print(n1 - n2) #subtract

#relational operators 
if n1 < n2 :
    print('n1 is less than n2')

if n2 > n1 :
    print('n2 is greater than n1')

if n1 == n3 :
    print('n1 and n3 are equal')

if n1 >= n3 :
    print('n1 is greater or equal to n1')

if n1 != n2 :
    print('n1 is not equal to n2')

if n1 == n3 : 
    print('n1 and n3 are equal')


#logical operators
#and = true when both values are true
#or = true when either of both values is true 
#not = reverses the values 

if n1 < n2 and n1 == n3 :
    print('and yeilds true')

if n1 < n2 or n1 == n3 :
    print('or yeilds true ')

if not n3 > n2:
    print('something')    


