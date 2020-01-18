
#get bot key in file : "/key.txt"
def getKey(fileName):
    #open file
    file = open(fileName)
    #read the first line of the file (there is only one)
    key = file.readline()
    #return the key
    return key