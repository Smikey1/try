import os
my_current_working_directory = os.getcwd()
print(my_current_working_directory)

orginal_path = r"C:Users\Smikey\Desktop\try"

# os.mkdir("any 2") # make new folder

# we can not make folder with same
# os.mkdir("any 2") # make new folder

# if(os.path.exists("any 2")):
#     print("already exist")
# else:
#     os.mkdir("any 5")


change_dir_path = r"C:\Users\Smikey\Desktop\DataBase"
os.chdir(change_dir_path) #--> Not working
print(f"Your current path--> {os.getcwd()}")

# Question to find the path of files:
for i in os.listdir(): # list out all
    file_path = os.path.join(os.getcwd(),i)
    print(f"The file path --> {file_path}")


# walk method --> walk in the path of files
# print(os.walk(orginal_path))
db_path = r"C:\Users\Smikey\Desktop\DataBase"
walked_result = os.walk(db_path)
for current_path,folder_names,file_name in walked_result:
    print(f"The current path --> {current_path}")
    print(f"The folder name --> {folder_names}")
    print(f"The file name path --> {file_name}")