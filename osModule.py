# Module os examples
#
import os

# List all the methods
print('List methods of os Module:')
print(dir(os))
print()

# List Path of Current Working Directory (CWD)
#    as a string
print('List CWD path:')
print(os.getcwd())
print()

# Change CWD
dir1 = '/Users/michaelkao/OneDrive/My_Projects'
print('Change CWD to:', dir1)
os.chdir(dir1)
print(os.getcwd())
print()

# List Contents of a Directory
#    CWD if no parm specified
dir1 = '/Users'
print('List contents of {0}:'.format(dir1))
print(os.listdir(dir1))
print()

# Create a Direcotry/folder
#   mkdir: create only one given dir
#   makedirs: create dirs all the way
dir1 = 'Demo-dir'
dir1sub = 'Sub-dir'
dirpath = os.path.join(dir1, dir1sub)

if not os.path.isdir(dirpath):
    os.makedirs(dirpath)
    print('{0} folder created in {1}.'.format(dir1, os.getcwd()))
    print(os.listdir())
    print()

    print('{0} folder created in {1}.'.format(dir1sub, dir1))
    print(os.listdir(dir1))
    print()

# List detail info of an object
from datetime import datetime

print('List info of:', dir1)
mod_time = os.stat(dir1).st_mtime
print('{0}\n\tModification time: {1}'.format(
    os.stat(dir1), datetime.fromtimestamp(mod_time)))
print()

# Remove a Direcotry/folder that is empty
#   rmdir: remove only one given dir
#   removedirs: Remove dirs all the way
if os.path.isdir(dirpath):
    os.rmdir(dirpath)
    print('{0} folder removed from {1}.'.format(dir1sub, dir1))
    print(os.listdir(dir1))
    print()

# Rename an object (folder or file)
dir2 = 'Demo-other-dir'
if os.path.exists(dir1) and not os.path.exists(dir2):
    os.rename(dir1, dir2)
    print('{0} folder renamed to {1}.'.format(dir1, dir2))
    print(os.listdir())
    print()

# clean up
if os.path.exists(dir1):
    os.removedirs(dir1)
if os.path.exists(dir2):
    os.removedirs(dir2)

# Directory tree tranversal
dir1 = '/Users/michaelkao/OneDrive/My_Projects/Python'

print('{} directory tree traversal:'.format(dir1))
for dirpath, dirname, filename in os.walk(dir1):
    print('Current Path:\t', dirpath)
    print('Directories:\t', dirname)
    print('Files:\t', filename)
    print()
