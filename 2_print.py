#outputting in different ways 
print('hello') #simple
print('hello i am "noor"')
print("""I'm reading "Hamlet" tonight.""") #triple quotes
print("""One 
Two
Three""") #multiple line

print(
    'one'    #with single quote 
) 

#exerise questions
print("python's the best!") 
print('the cat said "meow".')

#printing in a single line 
print('one ', end='')
print('two' , end='')

#printing in two lines 
print('\nmove'
      )

print('first\nsecond\nthird') #new line
print('mon\ttues\twed') #skip tab position
print('i m ready \'') #print a single quote
print('double quotes \"') #print double quotes
print('backslash\\') #print a backslash 

#breaking a string literal for concatenation = better readability
print('Enter the amount of ' + \
'sales for each day and ' + \
'press Enter.') #The \ at the end of a line tells Python that the line continues on the next line

#formatting floats 
#print numbers upto a certain decimal value 
n=12345.456789
print(n)
print(format(n, '.2f'))
print(format(n, '.1f'))
print(format(n, '.3f'))

#print numbers in scientific notation
print(format(n, 'e'))
print(format(n, '.2e'))

#print using comma separator = thousands place 
print(format(n, ',.2f')) 
print(format(n, ','))

#set precision
print('The number is', format(12345.6789, '12,.2f')) 
print('The number is', format(12345.6789, '12,')) 

#percentage 
print(format(0.5, '%')) #multplies number with 100 and places % sign 
print(format(0.5, '.0%')) #0 precision

#formatting ints
#annot tell precision as no comma and used instead of f as type designator 
print(format(12345, ',d')) #comma place
print(format(12345, '10d')) #move 10spaces , no comma
print(format(12345, '10,d')) #comma + move
