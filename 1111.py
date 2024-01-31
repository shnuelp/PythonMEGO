# import random
#
# numbers1 = random.sample(range(1, 101), 100)
#
# print(numbers1)
# numbers = []
#
# for i in range(100):
#   numbers.append(random.randint(0, 100))
#
# print(numbers)

# a=[i for i in range(100)]
# # a = [0] * int(input())
# # for i in range(len(a)):
# #     a[i] = int(input())
# print(a)



# n = int(input())
# length = 0
# while n > 0:
#     n //= 10  # this is equivalent to n = n // 10
#     length += 1
# print(length)  # 4

# i = 1
# while i <= 10:
#     print(i ** 2)
#     i += 1


# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# else:
#     print('Loop ended, i =', i)

# total_sum = 0
# a = int(input())
# while a != 0:
#     total_sum += a
#     if total_sum >= 21:
#         print('Total sum is', total_sum)
#         break
#     a = int(input())





"""
# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))"""
# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
"""
# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
a=sum(range(50))
print(a)

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
num = int(input("Enter the number: "))

if num > 1:
# check for factors
for i in range(2,num):
 if (num % i) == 0:
  print(num,"is not a prime number")
   print(i,"times",num//i,"is",num)
  break
 else:
  print(num,"is a prime number")
# if input number is less than
# or equal to 1, it is not prime
 else:
  print(num,"is not a prime number")
num = int(input("Enter the number: "))f

squares = [x**2 for x in range(1, 6)]
print(squares)
fruits = ['apple', 'banana', 'orange', 'kiwi']
filtered_fruits = [fruit.upper() for fruit in fruits if len(fruit) > 5]
print(filtered_fruits)
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
# Combine names and ages into a list of tuples
combined = list(zip(names, ages))
print(combined)
sentence = "Hello, how are you today?"
words = sentence.split(" t")  # Splitting at the comma delimiter
print(words)
sentence = "Hello   world!\tHow\nare you?"
words = sentence.split()
print(words)'
user_input = "   Hello, how are you?   "
words = user_input.split()
print(words)
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
    break
    print("Found an odd number", num)
# Python program to illustrate
# Iterating over a list
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
	print(i)

# Iterating over dictionary
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
	print("%s %d" % (i, d[i]))

# Iterating over a set
print("\nSet Iteration")
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
	print(i),
c=0
s = "Geeks"
for i in s:
    c=c+1
    print(i)
print(c)
from __future__ import print_function
for i in range(1, 20):
    for j in range(i):
        print(i, end=' ')
    print()
#Program to reverse a string
gfg = "geeksforgeeks"
print(gfg[1::-1])
# Joining with empty separator
list1 = ['g', 'e', 'e', 'k', 's']
print("".join(list1))

# Joining with string


# elements in tuples
list1 = ('1', '2', '3', '4')
print("-".join(list1))
import itertools
a = [[1, 2], [3, 4], [5, 6]]
b = list(itertools.chain.from_iterable(a))
print(b)
a=["10","9","8","7"]
print(a[::-1])
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[-3::-1])
a="Python is the language of the future"
b=a.split()
print(b)

a=10
b=20
print(f"first:  {a, b}")

a, b = b, a + 2
print(f"Second: {a, b}")

a, b, c = 1, 2, 3
print(a)
print(b)
print(c)


a = [x * 2 for x in range(10)]
print(a)

a = [1, 2, 3, 4 ,5]
b = a

# Change the 4th index in b
b = a[:]

print(id(a))
print(id(b))
print(a) # Remember we did not explicitly make changes to a.

x = 10
y = 20
print(f"{x = }, {y = }")


# x = 10, y = 20


a = ["english", "french", "spanish", "german", "twi"]
for language in a:
    print(language, end=" ")


english french spanish german twi
"""

a = [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 2, 2]
print(list(set(a)))

"""
[1, 2, 3, 4, 5, 6, 7]
"""

day = "04"
month = "10"
year = "2022"

print(day, month, year)
print(day, month, year, sep = "")
print(day, month, year, sep = ".")




"""
04 10 2022
04/10/2022
04.10.2022
"""
print(...)

list_of_strings = ["Hello", "my", "friend"]

# BAD:
list_of_strings = ["Hello", "my", "friend"]
my_string = " ".join(list_of_strings)
print(my_string)

colors = ["red", "green", "blue"]

c = "red"

# better:
if c in colors:
    print("is main color")

    print("Number Pattern ")

    # Decide the row count. (above pattern contains 5 rows)
row = 5
    # start: 1
    # stop: row+1 (range never include stop number in result)
    # step: 1
    # run loop 5 times
for i in range(1, row + 1, 1):
        # Run inner loop i+1 times
        for j in range(1, i + 1):
            print(j, end=' ')
        # empty line after each row
        print("")
names = ['Kelly', 'Jessa', 'Emma']
# outer loop
for name in names:
    # inner while loop
    count = 0
    while count < 5:
        print(name, end=' ')
        # increment counter
        count = count + 1
    print()

    # 5 rows
for name in range(5):
        # 3 column
        for j in range(3):
            print('*', end='')
        print()
import random

e = int(random.random()*100)
print(e)

def main():
    # מודפס הודעה למשתמש
    print("הזן מספרים. כדי לסיים, הקלד 'q'.")

    # משתנה לניהול מספר המספרים שנקלטו
    count = 0

    # משתנה לניהול הסכום של המספרים שנקלטו
    sum = 0

    # לולאה לקבלת מספרים מהמשתמש
    while True:
        # קולט מספר מהמשתמש
        number = input("הזן מספר: ")

        # אם המשתמש הקליד 'q', מסיים את הלולאה
        if number == "q":
            break

        # מוסיף את המספר לסכום
        sum += float(number)

        # מוסיף 1 למונה
        count += 1

    # אם לא נקלטו מספרים, הדפס הודעה
    if count == 0:
        print("לא נקלטו מספרים.")

    # אחרת, הדפס את הממוצע
    else:
        average = sum / count
        print("הממוצע הוא:", average)


if __name__ == "__main__":
    main()'''
def is_palindrome(word):

  בדיקה האם מחרוזת היא פלינדרום.

  Args:
    word: המחרוזת לבדיקה.

  Returns:
    True אם המחרוזת היא פלינדרום, False אחרת.


  i = 0
  j = len(word) - 1
  while i < j:
    if word[i] != word[j]:
      return False
    i += 1
    j -= 1
  return True


if __name__ == "__main__":
  word = input("הכנס מחרוזת: ")
  is_palindrome = is_palindrome(word)
  print("האם המחרוזת היא פלינדרום? ", is_palindrome)
import random

# יצירת רשימה של 100 מספרים אקראיים בין 0 ל-9, כולל
numbers = random.sample(range(0, 10),100)
n
# הדפסת המספרים האקראיים
print(numbers)



# More complex example
# for i in [1, 3, 5, 7, 9]:
#     x = i**2 - (i-1)*(i+1)
#     print(x, end=", ") # prints 1, 1, 1, 1, 1,

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()



#   # vowel string
# vowel_string = 'ae   io   u'
# # print(list(vowel_string))
#
# print(' '.join(vowel_string.split()[::2]))'''