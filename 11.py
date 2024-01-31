def different(list1, list2):
    # b=[]
    # for i in list1:
    #     if i not in b:
    #         if i not in list2:
    #         b.append(i)
    return list(set([i for i in list1 if i not in list2]))


def different1(list1, list2):
    list1.extend(list2)
    a = [i for i in range(101) if i not in list1]

    return a


#
#
list1 = [1, 2, 3, 2, 5]
list2 = [3, 4, 3, 3, 7]
print(different(list1, list2))
# print(different1(list1, list2))
# # #
# #
# # result = list(set(list1) - set(list2))
# # print(result)
# # #
# # #
# # list1 = ["a", "b", "c", "d", "e"]
# # list2 = ["a", "f", "c", "m"]
# # a = list(set(list2).difference(list1))
# # print(a)
#
# print("Welcome to my computer quiz!")
#
# playing = input("Do you want to play? ")
#
# if playing != "yes":
#     exit()



