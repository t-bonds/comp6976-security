'''
Created on Apr 7, 2020

@author: rockn
'''

import sys

print("Please enter a file name: ")
sys.argv

fileName = sys.argv[1]

#Substring that will be searched for in each line of the text file.
subString = "http"


#Open the file in read-only mode and store its contents in a variable. Then, print the number of lines
#in the file. Finally, close the file.
f = open(fileName, "r", encoding = 'utf-8', errors = 'ignore')
lines = f.readlines()
countOfLines = len(lines)
for line in lines:
    if line == '\n':
        countOfLines = countOfLines - 1
        
print("Total number of chat messages:", countOfLines)
f.close()


#Reopen the file in write-only mode and only write to the file the lines that contain
#the substring 'http'. Then, close the file and print how many lines contain links.
f = open(fileName, "w", encoding = 'utf-8', errors = 'ignore')
countOfLinks = 0
for line in lines: 
    if subString in line:
        countOfLinks = countOfLinks + 1
        f.write(line)
        
f.close()    
print("Total number of chat messages that contain links:", countOfLinks)
print("The file now only contains messages that have links in them.")

if __name__ == '__main__':
    pass