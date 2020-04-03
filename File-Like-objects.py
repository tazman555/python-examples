#!/bin/python
# File-Like Objects are used when you really need to have data in a file(because another function reqiures to read from a file)
# StringIO is file-object that will give file methods read and write but will be sotred in memory
# TO use StringIO you will need to import io library
import io
mystringfile = io.StringIO() #Fir handking bytes, ue io,bytesIO
mystringfile.write("This is my data!") # Write's data to object
print(mystringfile.read())     #Cursor is at the end!
print(mystringfile.seek(0))
print(mystringfile.read())

newstringfile = io.StringIO("My data") # The cursor will automatically reset to zero 
print(newstringfile)
print(newstringfile.read())

def iprintdata(f):
    print(f.read())

# iprintdata('mydata') # Does not work
my_io = io.StringIO('mydata')
iprintdata(my_io)