import os, sys, shutil

'''
This script is meant for the Math292 PreTeXt Textbook. 

Moves all HTML files + 'knowl' folder into the 'output' folder
'''

# path this script is allowed to run in
USE_FOR_PATH = "C" + sys.path[0][1:]

# check if this script is allowed to run
if os.getcwd() != USE_FOR_PATH:
    print("Directories do not match")
    print("Running may damage other directories")

cwd = os.getcwd() # current working dir
items = os.listdir() # list of items in cwd
newdir = "output" # dir relative to cwd to put stuff into

shutil.rmtree(os.path.join(cwd, newdir))
os.mkdir(os.path.join(cwd, newdir))

# move all html files into output
for item in items:
    oldpt = os.path.join(cwd, item)
    newpt = os.path.join(cwd, newdir, item)
    if item.endswith(".html"):
        os.replace(oldpt, newpt)

# move all files in knowl into knowl in output
old_kn = os.path.join(cwd, "knowl")
new_kn = os.path.join(cwd, newdir, "knowl")
shutil.move(old_kn, new_kn)

