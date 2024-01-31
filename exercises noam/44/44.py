def str4():

    while True:
        strt = 0
        str1 = input("Enter the string")
        if "T" not in str1:
            strt += 1

        if len(str1) < 4:
            break
    print(strt)


str4()
