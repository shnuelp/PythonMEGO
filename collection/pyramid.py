# width = 5
# for i in range(1, width * 2):
#     if i <= width:
#         print('* ' * i)
#     else:
#         print('* ' * (width * 2 - i))
# """
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
# """

# floors = 10
# width = floors * 2 - 1
# for i in range(floors + 1):
#     print("   " * (floors - i), end='')
#     print(" * "*(i * 2 - 1))
# """                      *
#                       *  *  *
#                    *  *  *  *  *
#                 *  *  *  *  *  *  *
#              *  *  *  *  *  *  *  *  *
#           *  *  *  *  *  *  *  *  *  *  *
#        *  *  *  *  *  *  *  *  *  *  *  *  *
#     *  *  *  *  *  *  *  *  *  *  *  *  *  *  *
#  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *
# """

# floors = 10
# width = floors * 2 - 1
# for i in range(floors + 1):
#     print("   " * (floors - i), end='')
#     print(" * " * (i * 2 - 1))
# for i in range(floors - 1, 0, -1):
#     print("   " * (floors - i), end='')
#     print(" * " * (i * 2 - 1))
#     """                
#                             *
#                          *  *  *
#                       *  *  *  *  *
#                    *  *  *  *  *  *  *
#                 *  *  *  *  *  *  *  *  *
#              *  *  *  *  *  *  *  *  *  *  *
#           *  *  *  *  *  *  *  *  *  *  *  *  *
#        *  *  *  *  *  *  *  *  *  *  *  *  *  *  *
#     *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *
#  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *
#     *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *
#        *  *  *  *  *  *  *  *  *  *  *  *  *  *  *
#           *  *  *  *  *  *  *  *  *  *  *  *  *
#              *  *  *  *  *  *  *  *  *  *  *
#                 *  *  *  *  *  *  *  *  *
#                    *  *  *  *  *  *  *
#                       *  *  *  *  *
#                          *  *  *
#                             *
#                             """


# a = 8
# for i in range(a + 1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
#
# a = [1,3,4,6, 7, 8, 3, 2, 12, 2, 2, 5, 6, 7, 1, 1, 2, 4 ]
# print(a)
# most = max(set(a), key=a.count)
# print (most
#
name = 'wow'
isPlaindrome = name.find(name[::- 1]) == 0
print(isPlaindrome)
