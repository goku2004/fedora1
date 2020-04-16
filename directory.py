import os
import sys
from os.path import isfile,join

DirPath = input()

s = os.listdir(DirPath)
for file in s:
    if isfile(join(DirPath,file)):
        print(file)
        
#We loop through every data(file) of the directory DirPath and then--
#--join the strings of file name and DirPath to verify whether these--
#--concatenated string is a file.If it is a file then we print that file.

#We concatenate the filename and DirPath because joining them will give us--
#--the path to the file....
