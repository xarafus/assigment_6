fname = input("Enter a file name: ")
try:
    with open(fname, 'r') as fhand:
        start = 0
        total_confidence = 0
        for line in fhand:
            if line.startswith("X-DSPAM-Confidence: "):
                confidence = float(line.split(":")[1])
                total_confidence += confidence
                start += 1
        if start > 0:
            average_confidence = total_confidence / start
            print("Average spam confidence: ", average_confidence)
except:
    print("File cannot be opened : ", fname)
