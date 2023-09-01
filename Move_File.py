import shutil
import os
from_directory=r'C:\Users\dhruv\Downloads'
to_directory=r'C:\Users\dhruv\OneDrive\Desktop\Python Coding\Class 111 Homework'
listOfFiles=os.listdir(from_directory)
print(listOfFiles)
for pdf_name in listOfFiles:
    name,extention=os.path.splitext(pdf_name)
    if extention=="":
        continue
    if extention in [".pdf"]:
        path1=from_directory+"/"+pdf_name
        path2=to_directory+"/"+"pdf_files"
        path3=to_directory+"/"+"pdf_files"+"/"+pdf_name
        if os.path.exists(path2):
            print("moving")
            shutil.move(path1,path3)
        else: 
            os.makedirs(path2)
            shutil.move(path1, path3)        