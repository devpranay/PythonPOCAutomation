"""9. Create, update, move, and rename files and folders?"""
import os
import shutil
s=os.getcwd()
os.mkdir("c://py-practise3-os")
os.rename("c://py-practise2-os//ex-2","c://py-practise2-os//ex-3")#rename to sub folder
os.mkdir("c://py-practise-os//py-file")#create a sub folder
os.rename("c://py-practise-os","c://py-practice-os")#rename to folder
shutil.move("c://py-practise-os//ex-2.py","c://py-practice-os")#move files
shutil.rename("c://py-practise2-os","c://py-practice-os")#rename to folder
os.rename("c://py-practise-os","py-practice2-os")#rename folder without mention drive
shutil.move("c://py-practise-os//ex-4.py","d://py-practise-os")# another drive
file=open("c://py-practise3-os//task_file.py","x")# create a file
file.close()
