#----Files in Python----

#1) Open a File:
f = open("test.txt")#same directory
print(f.read())
f = open(" C:\PYTHON\Chapter 29 Basic Input and Output\test.txt")#different directory
print(f.read())

#2) Reading Data from the File
f = open("test.txt", 'r')
print(f.read())#print whole file
print(f.readline())#To read only one line

#3) Writing Data to File
f = open("test.txt", 'w')
f.write("Hello Python \n")
f.write("Hello World")
f = open("test.txt")#same directory
print(f.read())

#4) Close a File
f = open("test.txt", 'r')
print (f.read())
f.close()

#5) Create & Delete a File
f = open("file.txt", "w")#created
f.close()

import os   #Removing
os.remove("file.txt")
