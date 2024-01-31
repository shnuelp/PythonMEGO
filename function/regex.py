# pattern = '^a...s$'
# test_string = 'abyss'
# result = re.search(pattern, test_string)
#
# if result:
#   print("Search successful.")
# else:
#   print("Search unsuccessful.")
#

# Substring = 'string'
#
# String1 = '''We are learning regex with geeksforgeeks
#          regex is very useful for string matching.
#           It is fast too.'''
# String2 = '''string We are learning regex with geeksforgeeks
#          regex is very useful for string matching.
#           It is fast too.'''
#
# # Use of re.search() Method
# print(re.search(Substring, String1))
# # Use of re.match() Method
# print(re.match(Substring, String1))
#
# # Use of re.search() Method
# print(re.search(Substring, String2,))
# # Use of re.match() Method
# print(re.match(Substring, String2))

# caret sign -> the start of the str
# dollar sign -> the end of the string

# pattern = r'^H...o$'
#
# text_string = "Hello World"
#
# if re.search(pattern, text_string):
#     print(f"{text_string} ends with 'world'")
# else:
#     print(f"{text_string} does not end with 'world'")


#
# def validating_name(name):
#   regex_name = re.compile(r'^(Mr\.|Mrs\.|Ms\.) ([a-z]+)( [a-z]+)*( [a-z]+)*$',
#                           re.IGNORECASE)
#   res = regex_name.search(name)
#
#   if res:
#     print("Valid")
#
#   else:
#     print("Invalid")
#
# # Driver Code
# validating_name('Mr. Albus Severus Potter')
# validating_name('Lily and Mr. Harry Potter')
# validating_name('Mr. Cedric')
# validating_name('Mr. sirius black')

# if re.search(r"[Rr]egex", "regex are awesome"):
#     print("found a match")
# else:
#     print("no match")

#
import re

file = ["shmtuel.bgfb", "abtc.jpg","!abtc.jpg", "youtugbe.jpeg", "gtgrg8u8.ppng", "0o))5364.gif"]

for filename in file:
    is_valid = re.match(r"^[a-zA-Z0-9][a-zA-Z0-9_\-()]*\.(jpg|jpeg|png|gif)$", filename)
    if is_valid:
        print(f"{filename}: True")
    else:
        print(f"{filename}:  False ")


def is_filename_safe(filename):
    regex = '^[a-zA-Z0-9][a-zA-Z0-9() _- ]*(\jpg |\,jpeg |\.png |.gif )$'
    return re.match(regex, filename) is not None

Print(is_filename_safe('_my_file-(image).jpg' ) )






