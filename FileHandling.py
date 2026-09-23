'''
What is File Handling?
---> File handling is used to save file in permenent in file because file is in read, write, append and closed

we used 4 Files 
pdf, csv, text, json, excel

file modes
w = write
r = read
a = append(write)
x = create
w+ = write and read
r+ = read and write
'''
file = open("text.txt","w")
my_file = file.write("This is new file")
print(my_file)
file.close()

file = open("text.txt","r")
print(file.read())
file.close()

file = open("text.txt","a")
data = file.write("KJ College Of Engineering")
print(data)
file.close()

file = open("text.txt", "r")
for i in file:
    print(i)

file = open("text.txt","r")
my_file = file.read()
print(my_file)
file.close()

# how file in read and write = r+
with open("test.txt","r+") as file:
    file.write("This is File")
    print(file.readline())

with open("test.txt","r") as file:
    data = file.readline()
    print(data.upper())

# how file in write and read = w+
with open("test.txt","w+") as file:
    file.write("This is File")
    print(file.readline())

with open("test.txt","r") as file:
    data = file.readline()
    print(data.upper())

#Now csv files
import csv
with open("test.txt","r") as file:
    myfile = csv.reader(file)
    x = next(myfile)
    for row in x:
        print(row)

#Now Json Files
import json
file = open("post.json","r")
my_file = file.read()
x = json.loads(my_file)
print(x)