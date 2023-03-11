import shutil
import os
path = 'C:\Users\alikh\OneDrive\Рабочий стол\pp2\tsis6\dir\8.txt'
if os.path.exists(path):
    print("this path exists")
   
    shutil.rmtree(path)
else:
    print("this path doesn't exists")