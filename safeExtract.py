
import re
from pysafebrowsing import SafeBrowsing
import sys


fileName = sys.argv[1]
s = SafeBrowsing("AIzaSyC5zRGDds2v6--ZlDDyM274sv1Ueg4jC9M")

f = open(fileName, "r", encoding = 'utf-8', errors = 'ignore')
lines = f.readlines()
for line in lines:
    link = re.findall(r'(https?://[^\s]+)', line)
    r = s.lookup_urls(link)
    print(str(r))
    w = open("safelink.txt", "a+", encoding = 'utf-8', errors = 'ignore')
    w.write(str(r)+"\n")
    w.close()
    line.strip()
f.close()
