outputfile = open(" Uploaded.txt", "w")
inputfile = open("file.txt", "r")
lines_scenes_so_far = set()
print("Elimination of duplicate lines....")
for line in inputfile:
     if line not in lines_seen_so_far:


            outputfile.write(line)

lines_seen_so_far.add(line)

inputfile.close()
outputfile.close()