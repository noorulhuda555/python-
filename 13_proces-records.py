def writerecord():
    num = int(input('no. of employees?'))

    empfile=open('empfile.txt', 'w')
    for count in range(1, num+1):
        print('enter data for emp ', count, sep='')
        name=input('name: ')
        id=input('id:')

        empfile.write(name+ '\n')
        empfile.write(id + '\n')
        print()

    empfile.close()    
    print('check empfile now !')

writerecord()

def readrecord():
    empfile=open('empfile.txt', 'r')
    name=empfile.readline()
    while name!= '':
        id=empfile.readline()
        name=name.rstrip('\n')
        id=id.rstrip('\n')
        print('name : ' , name)
        print('id :', id) 
        print()
        name=empfile.readline()
    empfile.close()

readrecord()

    