import glob

readFiles = glob.glob("/Users/t.bonds/Desktop/dup1/*")

readFiles = set(readFiles)
with open("channels.txt", "a+") as w:
    for n in readFiles:
        w.write(str(n)+ "\n")
    w.write("Number of Channels: "+ str(len(readFiles)))    
print(readFiles)
print(len(readFiles))
