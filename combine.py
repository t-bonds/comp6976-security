import glob

readFiles = glob.glob("/Users/t.bonds/Desktop/dup/*/*/*.log")
#print(readFiles)
#print(len(readFiles))

with open ("result_log.txt", "wb") as outfile:
    for f in readFiles:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
