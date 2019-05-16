import os
import os.path
import shutil

listdirs = []
for current_dir, dirs, files in os.walk("main"):
    if any([file[-3:] == '.py' for file in files]):
        listdirs.append(current_dir)
listdirs.sort()
for l in listdirs:
    print(l)
