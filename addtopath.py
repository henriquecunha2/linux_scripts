#!/usr/bin/python3

import os, sys, fileinput

HOME = (os.environ['HOME'])
BASH_FILE = "{}/.bashrc".format(HOME)
EXPORT_PATH = "export PATH="

def no_file_error():
    '''
    Prints an error message if the user does not provide a file or directory
    '''
    print("You need to provide SOME file or directory to be added to the PATH")
    sys.exit()

def wrong_file_error():
    '''
    Prints an error message if the user does not provide a valid file or directory
    '''
    print("Provide a VALID file or directory, please")
    sys.exit()

# If no argument is provided
try:
    PATH_TO_FILE = sys.argv[1]
except IndexError:
    no_file_error()

# If a blank argument is provided (don't know if this is possible)
if PATH_TO_FILE == "":
    no_file_error()

# If the user provides a path to a file or dir that does not exist
if (not os.path.isdir(PATH_TO_FILE)) and (not os.path.isfile(PATH_TO_FILE)):
    wrong_file_error()

found_line = False
new_line = ""
for line in fileinput.input(BASH_FILE, inplace=True):
    if EXPORT_PATH in line:
        found_line = True
        new_line = "{}:{}\n".format(line[:len(line)-1], PATH_TO_FILE)
        line = line.replace(line, new_line)
    sys.stdout.write(line)

if not found_line:
    new_line = "{}$PATH:{}".format(EXPORT_PATH, PATH_TO_FILE)
    with open(BASH_FILE, "a") as file:
        file.write("\n" + new_line)

