import re
import sys


fileName = sys.argv[1]

f = open(fileName, "r", encoding = 'utf-8', errors = 'ignore')
lines = f.readlines()
for line in lines:
    link = re.findall(r'(https?://[^\s]+)', line)
    print(str(link))
    w = open("links.txt", "a+", encoding = 'utf-8', errors = 'ignore')
    w.write(str(link)+"\n")
    w.close()
f.close()
