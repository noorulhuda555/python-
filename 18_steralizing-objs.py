"""converting objects into a stream of bytes 
that can be saved to a file for later retrieval
process is also called pickling

module named pickle is used 

open in binary mode (wb)
use dump method to pickle and write it
close after saving



"""
import pickle


#pickle.dump(object, file)

studentid={'noor': 3, 'maria': 2, 'sara' : 5}
outputfile=open('studentid.dat', 'wb')
pickle.dump(studentid, outputfile)
outputfile.close()

inputfile=open('studentid.dat', 'rb')
pb= pickle.load(inputfile)
print(pb)

