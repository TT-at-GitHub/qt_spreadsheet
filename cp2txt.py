import os
import sys 
import shutil


def copytree(src, dst, symlinks=False, ignore=None):

    for item in os.listdir(src):
        if item == '__pycache__':
            continue
        s = os.path.join(src, item)
        d = os.path.join(dst, item)

        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

dst = './.ignore/qspreadsheet.txt/'
if os.path.isdir(dst):
    shutil.rmtree(dst)
    
os.mkdir(dst)
copytree('qspreadsheet/', dst)


for fd in os.listdir(dst):
    os.rename(os.path.join(dst, fd), os.path.join(dst, fd + '.txt'))