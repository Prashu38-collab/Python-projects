import os
import shutil

Source_folder="/Users/prashamsaghimire/Desktop/test_folder"
FILE_TYPES={
    "Images":[".img",".jpeg",".jpg",".png"],
    "Files":[".pdf",".docx",".txt"],
    "Music":".mp3",
    "Video":".mp4"}

'''' os.listdir= list all file and folder in the specified directory'''

for filename in os.listdir(Source_folder): #filename: images.jpg,w.pdf
    file_path=os.path.join(Source_folder,filename) #source folder : test_folder
    if os.path.isfile(file_path): #  filepath: fullpath users/tes_folder/images.jpg
        file_ext=os.path.splitext(filename)[1].lower() #retriving only the extension and stroing in variable file ext
        for folder_name,extension in FILE_TYPES.items(): #iterating through dict key: folder_name, vALUE: extension
            if file_ext in extension: # checking if extension is present in values
                target_folder=os.path.join(Source_folder,folder_name) # if yes creating a new folder named through keys 
                os.makedirs(target_folder,exist_ok=True) #making new onw if it doesnt exists
                shutil.move(file_path,target_folder)  # moving the full path file to respective folders
                break 
