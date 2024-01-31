def check_word(address):
    with open("../text.txt", mode="r") as file:
        contents = file.read()
        text1 = contents.split()
        # print("original text in list: ", text1)
        new_text = []
        string = ""
        for i in text1:
            for j in i:
                if j.isalpha():
                    string += j
            print(string)
            new_text.append(string)
            string = ""
        print(new_text)

    letter_frequency = dict()
    strr = ""
    str1 = 0
    for letter in new_text:
        if letter.isalpha():
            letter_frequency.setdefault(letter, 0)
            letter_frequency[letter] += 1

    print("Number of words:", len(new_text))
    for i in letter_frequency:
        strr += f"{i} ,{letter_frequency[i]}\n "
        if letter_frequency[i] == 1:
            str1 += 1
    print(f"Number of words unique :{str1}")
    print(strr)


adress = input("Enter the file path:")
check_word(adress)

# str1 = "Apple gfgfsdg     fgfdgsfdg  fgfdgsfdg"
#
# # create a result dictionary
# char_dict = dict()
#
# for char in str1.split():
#     count = str1.count(char)
#     # add / update the count of a character
#     char_dict[char] = count
# print('Result:', char_dict)
