new_file=open('newfile.txt','x')
new_file.close()
import os
print("Checking if my file exists or not")
if os.path.exists('myfile.txt'):
    os.remove('myfile.txt')
else:
    print("The file does not exist")

my_file=open('myfile.txt','w')
my_file.write("Hi! I am Penguin and I am 11 years old.")
my_file.close()

os.remove('Sample.txt')