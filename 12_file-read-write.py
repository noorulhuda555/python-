file_name = open('myfile.txt', 'r' ) #open to read 
#sales_file = open('sales.txt', 'w') #open to write 

#writing to a file
"""sales_file.write('20\n')
sales_file.write('30\n')
sales_file.write('40\n')
sales_file.write('50\n')"""
#file_name.write('adding a new file')#erro bcz mode is read

def filefunctionwrite():
    outfile = open('names.txt', 'w')
    outfile.write('noor the superstar\n')
    outfile.write('maria the baka\n')
    outfile.write('mama the sunflower\n')
    outfile.write('papa the only braincell')

    outfile.close()

def filefunctionread():
    infile = open('names.txt', 'r')
    content = infile.read()
    infile.close()
    print(content)
    
def filefunctionbyline():
    infile = open('names.txt', 'r')
    line1=infile.readline()
    line2=infile.readline()
    line3= infile.readline()
    line4=infile.readline()
    
    infile.close()
  
    print('printing line by line this time')
    print(line1)
    print(line2)
    print(line3)
    print(line4)

def concatenating(): #using input function
    print('enter 3 whatever things')
    thing1=input('things # 1: ')
    thing2=input('things # 2: ')
    thing3=input('things # 3: ')    

    thingy = open('things.txt', 'a')

    thingy.write(thing1 + '\n')
    thingy.write(thing2 + '\n')
    thingy.write(thing3 + '\n')

    thingy.close()
    print('check the thingy file now')

def useloop():
    sales = open('sales.txt', 'r')
    for line in sales:
        amount = float(line)
        print(format(amount, '.2f'))
    sales.close()



#filefunctionwrite()
#filefunctionread()
#filefunctionbyline()
#concatenating()
useloop()
