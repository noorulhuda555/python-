# small chunks of code to perform certain task(S)
# code blocks 
# scope of a function is indicated by indentation

import random
import math

my_value = 10 #global varible can be accessed anywhere
#void functions 
def main():
    value = 5  #local variable 
    show_double(value)  #call to dhow double function
    print('im showing my value in main :', my_value)

def show_double(num):
    result=num*2
    print(result)
    print('im showing my value in show double', my_value)

main() # call to main function 

#output : 10

#value - returning functions 
def get_random_num():
    number = random.randint(1,10) #using random module random library has randint func access by . operator 
    print('printing a random number ', number)

get_random_num()    

def sum(n1 , n2):
    sum=n1+n2
    return sum

print('sum of 2 ans 3', sum(2,3))

def hypot():
    a= float(input('enter side a '))
    b= float(input('enter side b '))
    c=math.hypot(a, b)
    print('hypotenus is ', c)


hypot()
#math library has many other functions for mathematical operations 


print('exercise ---------')
def main():
    x = 1
    y = 3.4
    print(x, y)
    change_us(x, y)
    print(x, y)
def change_us(a, b):
    a = 0
    b = 0
    print(a, b)

main()


