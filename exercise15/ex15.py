#imports argv module
from sys import argv

#sets variables for argv
script, filename = argv

#sets variable txt that is opening argument 'filename" when running the script.
txt = open(filename)

#This prints the string and includes the actual filename added as an argument when running the script
print "Here's your file %r:" % filename
#This references the variable txt which opens filename and then prints out it's contents on the screen
print txt.read()

#This repeates the process above by asking me to type the filename and sets it as "file_again" variable
print "Type the filename again:"
file_again = raw_input("> ")

#This takes the above input and opens the file
txt_again = open(file_again)

#This takes the open file and prints it's contents on the screen
print txt_again.read()
txt_again.close()
txt.close()
