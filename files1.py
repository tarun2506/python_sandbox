#open a file
myfile = open('tarun.txt', 'w')

#get some info

print('Name:', myfile.name)
print("Is closed:", myfile.closed)
print("Opening mode:", myfile.mode)


#Write to file

myfile.write("Hello world")
myfile.write(" Tarun here")
myfile.close()

#Append to file

myfile = open('tarun.txt', 'a')
myfile.write(' I also like velocity')
myfile.close()

#read from file

myfile = open('tarun.txt', 'r')
text = myfile.read()

print(text)