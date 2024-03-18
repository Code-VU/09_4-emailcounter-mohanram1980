def countEmail():
    # This first line is provided for you
    name = input("Enter file:")

    if len(name) < 1: name = 'mbox-short.txt'
          
    mbox_file = open(name)

    fromDict = {}
    for line in mbox_file:
        line = line.strip()
        if line. startswith("From " ):
            sender = line.split()[1]
            if sender not in fromDict:
                fromDict[sender] = 1
            else:
                fromDict[sender] += 1

        dictVals = fromDict.values()
        maxVal = max(dictVals)
        print(max(fromDict, key=fromDict. get), maxVal)

## if you want to test locally run > python counter.py
if __name__ == "__main__":
    countEmail()