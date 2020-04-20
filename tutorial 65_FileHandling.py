# File Handling --
# Read from another file
# Write to another file
# Read and Write Image

file1 = open('naveen', 'r') # Read from another file
print(file1.read())
#print(file1.readline())

f = open('naveen', 'w') # Write to another file
#f.write('new line added')

f1 = open('naveen', 'w')
f1.write('Naveen Kumar Sambandan')
f2 = open('naveen', 'a') # appending in file
f2.write('Mageswari Kasinathan')
f2.write('good life')



file2 = open('Picture1.JPG', 'rb') # Read image file
#print(file2.read())
#for i in file2:
#    print(i)

file3 = open('Picture_3.JPG', 'wb') #Write image file
for i in file2:
    file3.write(i)