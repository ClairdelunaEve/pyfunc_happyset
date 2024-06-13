import os
import shutil

# Write
def Write_a_1dlist(filepath,writelist,delimiter):
    writelist = [str(i) for i in writelist]
    with open(filepath,'a') as f:
        f.write(delimiter.join(writelist))

def Write_a_2dlist(filepath,writelist,delimiter):
    for row in writelist:
        row = [str(i) for i in row]
        with open(filepath,'a') as f:
            f.write(delimiter.join(row)+"\n")

def Write_w_1dlist(filepath,writelist,delimiter):
    writelist = [str(i) for i in writelist]
    with open(filepath,'w') as f:
        f.write(delimiter.join(writelist))

def Write_w_2dlist(filepath,writelist,delimiter):
    Clear_file(filepath)
    for row in writelist:
        row = [str(i) for i in row]
        with open(filepath,'a') as f:
            f.write(delimiter.join(row)+"\n")

# Clear
def Clear_dir(path):
    shutil.rmtree(path)
    os.mkdir(path)
    
def Clear_file(path):
    with open(path, "r+") as f:
        f.truncate(0)

# Copy
def Copy_dir(targetPath, createPath):
    shutil.copytree(targetPath, createPath, dirs_exist_ok=True)

# Move
def Move_file(srcpath, dstpath):
    shutil.move(srcpath, dstpath)
