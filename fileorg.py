import os 
import shutil

path=input ("Enter Path: ")

files=os.listdir(path)

for file in files:

    filename,extension=os.path.splitext(file)

    extension=extension[1:]

    if os.path.exists(path+'/'+extension):

        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)

    else:

        os.makedirs(path+'/' +extension)

        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
        
print("your files are sorted\n")   
ans=input (print("do you want to delete any folder (y/n): ")) 
if ans=="y":    
    ch=input (print("Type extension name:"))


    directory_path = path+'\\'+ch
    #"/"=="\\" both are same 
    #python will support "/" by this code can work in any platfrom

    # Check if the directory exists
    if os.path.exists(directory_path):
        shutil.rmtree(directory_path)
        print(f'Directory {directory_path} and all its contents deleted.')
    else:
        print(f'Directory {directory_path} does not exist.')
else:
    exit     
        
        