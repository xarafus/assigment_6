fhand = open("C:/Users/xarafus/Documents/GitHub/Computational-Thinking-and-Programming/mbox.txt","r")
count = 0
for line in fhand:
    if line.startswith("From: "):
        signat = line.find("@")
        foundd = line.find(" ", a)
        print(line[a+1:b])
        count += 1
print("Total %d hosts printed" %(count))
fhand.close()
