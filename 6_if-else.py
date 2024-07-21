#decision control structures 
n1 = 2
n2 = 4
#syntax of if is given below 
#if condition : 
#scope of if is within the indentation of code blocks
#variables within if can be accessed outside 
if n1 > n2 :
    print('n1 is less than n2')
print('checking...') #will be printed either ways unless indented
                  #under the if 

if n1 == n2 :
    print('they are equal')
else :
    print('they are not equal')

x = 10
if x > 5:
    y = x * 2
else:
    y = x / 2

print(y)  # y is accessible here because it is defined in both the if and else blocks

x = 3

if x > 5:
    y = x * 2

print(y)  # This will raise an error because y is not defined if x <= 5

x = 3
y = None

if x > 5:
    y = x * 2

print(y)  # y is defined as None if x <= 5

#compares ascii values below and prints else statement
#z=122, a=97
if 'z' < 'a':
    print('z is less than a.')
else:
    print('z is not less than a.')

s1 = 'New York'
s2 = 'Boston'
if s1 > s2 : 
    print(s2)
    print(s1)
else:
    print(s1)
    print(s2)    

#he first character of s1 ("New York") is 'N', and its ASCII value is 78.
#The first character of s2 ("Boston") is 'B', and its ASCII value is 66.
#Since 78 > 66, s1 > s2 evaluates to True. Therefore, the if condition will be satisfied

