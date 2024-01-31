# # r - reading
# # w - writing
# # r+ - read & write
# # w+ - writing, creates a new file if doesn't exist
# # a - writing, appending, creates
# # x - created only if does not exist, writing
#
# # aka "exclusive creation"
# file = open("abc.txt", "a")
# contents = file.write("fhgfhgv")
# print(contents)
#
# with open("abc.txt") as file:
#     contents = file.read()
#     print(contents)
#
# with open("abc.txt", mode="w+") as file:
#     file.write("I am Groot!")
#
# # contents = file.read()
# # print(contents)
#
# with open("abc.txt") as file:
#     contents = file.read(abc.txt)
#     print(contents)
#
# שורה שורה
# myfile = open("demo.txt", "r")
# myline = myfile.readline()
# while myline:
#     print(myline)
#     myline = myfile.readline()
# myfile.close()
#
# myfile = open("test.txt", "r")
# mylist = myfile.readlines()
# print(mylist)
# myfile.close()
#
# myfile = open("test.txt", "r")
# for line in myfile:
#     print(line)
# myfile.close()
#
# # העתקת קובץ
# with open('test. txt', 'r') as rf:
#     with open('test_copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)
# העתקת תמונה
# with open('bronx.jpg', 'rb') as rf:
#     with open('bronx_copy.jpg', 'wb') as wf:
#         for line in rf:
#             wf.write(line)
