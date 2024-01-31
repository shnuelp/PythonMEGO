def string():
    sumx = 0
    while True:
        strinput = input("enter the string ")
        if strinput[:1] == "x" and strinput[-1] == "x":
            sumx += 1
        if strinput == "Z":
            break
    return sumx

print(string())