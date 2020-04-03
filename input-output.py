#!/bin/python
#Input and output w+= write creat file, w=over write existing, r=read, r+= read and write, b= binary mode
# Create and write data to a file
myfile = open('data.txt', 'w+')
myfile.write("I am writing data to my file")
myfile.close()

# over write existing file, will erase existing data
myfile = open('data.txt', 'w')
myfile.write("I am writing data to my file\n")
myfile.close()

# Append data
myfile = open('data.txt', 'a')
myfile.write("I am writing additional data to my file\r\n")
myfile.close()

# Read data form file
myfile = open('data.txt', 'r')
x = myfile.read()
myfile.close()
print(x)

# Example how to insert 10 lines in a file
for i in range(10):
    myfile = open('data.txt', 'a')
    myfile.write("This is a test %d\r\n" % (i+1))

myfile = open('data.txt', 'r')
x = myfile.read()
myfile.close()
print(x)

# Using with command to make sure file is closed after
with open('data.txt') as f:
    print(f.read())

# Reading lines from a file
line_file = open('fewlines.txt', 'w+')
line_file.writelines("first\n")
line_file.writelines(["second\n", "third\n"])
line_file.close()
line_file = open('fewlines.txt', 'r')
print(line_file.readline())
print(line_file.readline())
print(line_file.readline())
print(line_file.readline())
line_file.close()
line_file = open('fewlines.txt', 'r')
y = line_file.read()
print(y)

input_file = open('data.txt', 'r')
print(input_file.tell())
print(input_file.read(6))
print(input_file.tell())
print(input_file.seek(0))
print(input_file.read())