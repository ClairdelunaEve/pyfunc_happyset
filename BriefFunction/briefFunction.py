import csv
import os
import shutil
import itertools
import re
import time

def Get_csv2List(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        data = [data for data in reader]
    return data

def Get_text2list(path,delimiter):
    with open(path, 'r') as f:
        return f.read().split(delimiter)

def Conv_2dListTo1dList(l_2d):
    return list(itertools.chain.from_iterable(l_2d))

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

def Get_dirList(path):
    return sorted([f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))])

def Get_fileList(path):
    return sorted([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and (not f.startswith("."))])

def Get_filepathList(path):
    return sorted([os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and (not f.startswith("."))])

def Get_uniqueList(targetList):
    return sorted(filter(lambda a: a != '',list(set(targetList))))

def Get_keysFromValue(d, val):
    return [k for k, v in d.items() if v == val]

def Clear_dir(path):
    shutil.rmtree(path)
    os.mkdir(path)
    
def Clear_file(path):
    with open(path, "r+") as f:
        f.truncate(0)

def Copy_dir(targetPath, createPath):
    shutil.copytree(targetPath, createPath, dirs_exist_ok=True)

def Move_file(srcpath, dstpath):
    shutil.move(srcpath, dstpath)

def Replace_match(sentence, targetWord, replaceWord):
    match = re.search(targetWord,sentence)
    if match:
        return sentence.replace(match.group(),replaceWord)
    else:
        return sentence

def Wait(sec):
    time.sleep(sec)

