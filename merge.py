import ast
import sys

fileName = sys.argv[1]

lines = []
with open(fileName, "r", encoding = 'utf-8', errors = 'ignore') as file:
    lines = file.readlines()
#print(lines)

link = []
for line in lines :
    link.extend(ast.literal_eval(line))
link = set(link)
with open("linkList.txt", "a+", encoding = 'utf-8', errors = 'ignore') as w:
    for l in link:
        w.write(str(l)+"\n")
#print(link)
