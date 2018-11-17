from hashlib import *
file=input("enter the file name : ")
with open(file,mode="r") as f:
    
    for line in f:
        line=line.strip()
        hashfile=md5(line.encode()).hexdigest()
        print(hashfile)
