# loop inside another loop

#for hours in range(24):
#    for minutes in range(60):
#        for seconds in range(60):
#           print(hours, ':', minutes, ':', seconds)

print('pattern 1 ')
for r in range(6):
    for c in range(6):
        print('*', end='')
    print()

print('pattern 2 ')


for r in range(9):
   #print(r)
    for c in range(r+1):
        print('*', end='')
    print()    

print('pattern 3')

for s in range(5):
    for st in range(s+1):

        print(' ', end='')

    print('#')    #end char

print('pattern 4')

for r in range(8,0,-1):
    for c in range(r):
        print('*', end='')
    print()

print('pattern 5')

for s in range(6):
    print('#', end='')
    for t in range(s+1):
        print(' ', end='')
    print('#')
   

        