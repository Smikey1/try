'''
Working with files:

#methods:
1) readFile
2) open function vs with block--> takes path
3) read function
4) seek function  --> change the position of cursor
5) tell function  --> find the position of cursor
6) readline vs readlines method/function
'''

poem_path = r"python-poem.txt"

# open function: # bydefault read mode
rf=open(poem_path)
rf.close()

# it automatically close when done.
with open(poem_path) as rf:
    pass


'''
rf=open(poem_path)
print(f"Before reading, cursor position:-->{rf.tell()}")
print(rf.read())
print(f"After reading, cursor position:-->{rf.tell()}")
print("-----------------------------------------")
rf.seek(0)
print(f"Seek reading, cursor position:-->{rf.tell()}")
# print(rf.read())


print(f"Next line --> {rf.readline()}")
print("------------------------")

print(f"Next line --> {rf.readline()}", end="")
print("------------------------")


# readlines method
all_lines = rf.readlines()
print(all_lines)

for line in all_lines:
    print(f"The line: --> {line}",end="")

rf.close()
'''

'''
Write data in file with (w,a,r+ mode)
'''

# write mode
# --> delete all previous data and write with new data
# with open(poem_path,"w") as wf:
#     wf.write("Ok, Thik xa")

# # append mode
# # --> not delete all previous data and write with new data in last
# with open(poem_path,"a") as af:
#     af.write("\nla la")

abc_path = r"abc.txt"

# r+ mode
# --> not delete all previous data and write with new data in last
# with open(poem_path,"r+") as rpf:
#     rpf.write("Write r+ data")

# with open(abc_path,"r+") as rpf:
#     rpf.seek(5)
#     rpf.write("mmmmmmmm")



# read and write--> same time

with open(poem_path,"r") as rf:
    with open(abc_path,"w") as wf:
        wf.write(rf.read())

# read love story
love_story_path = r"love_story.txt"

with open(love_story_path,"r",encoding="utf-8") as rf:
    print(rf.encoding)
    print(rf.read())



ok_path = r"ok.txt"
yes_path = r"yes.txt"

rf=open(poem_path)
all_lines = rf.readlines()
print(all_lines)
rf.close()

# Challange excersice
with open(ok_path,"r") as rf:
    with open(yes_path,"w") as wf:
        for line in rf.readlines():
            name,salary=line.split(",")
            print(line)
            wf.write(f"{name} earns monthy {salary} we are ok")