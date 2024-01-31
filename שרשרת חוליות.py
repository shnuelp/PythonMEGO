# class IntNode:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next
#
#     def get_value(self):
#         return self.value
#
#     def get_next(self):
#         return self.next
#
#     def set_value(self, value):
#         self.value = value
#
#     def set_next(self, next):
#         self.next = next


# maximom = 0
# sum = 0
# cuont = 0

# first = None
#
# for i in range(4, 0, -1):
#     first = IntNode(i, first)
#     sum += first.get_value()
#     cuont += 1
#     if first.get_value() > maximom:
#         maximom = first.get_value()
# #
# temp = first
# while temp != None:
#     print(temp.value_to_string())
#     temp = temp.get_next()
# print()
# # print(sum)
# # print(cuont)
# # print(maximom)

# def length(first,num):
#     len = 0
#     temp = first
#     while temp != None:
#         if temp.get_value() == num:
#             len += 1
#         temp = temp.get_next()
#     return len
#
# num =2
# first = None
#
# first = IntNode(2, first)
# first = IntNode(2, first)
# first = IntNode(3, first)
# first = IntNode(3, first)
# first = IntNode(4, first)
# first = IntNode(5, first)
# print(length(first,num))

# def length(first):
#     sum = 0
#     len = 0
#     temp = first
#
#     while temp != None:
#         sum += temp.get_value()
#         len += 1
#         temp = temp.get_next()
#     return  sum // len
# #
# #
# first = None
#
# first = IntNode(2, first)
# first = IntNode(2, first)
# first = IntNode(3, first)
# first = IntNode(3, first)
# first = IntNode(4, first)
# first = IntNode(5, first)
# # print(length(first))
# node1 = IntNode(10)
# node2 = IntNode(20)
# node3 = IntNode(30)
# node4 = IntNode(40)
# node5 = IntNode(50)
#
# node1.next = node2
# node2.next = node5
# node3.next = node4
# node4.next = node5
#
# temp = first
# while temp != None:
#     print(temp.get_value())
#     temp = temp.get_next
#
# class Node:
#     def _init_(self, data=None):
#         self.data = data
#         self.next = None
#
# # Sample data
# data_list = [5, 10, 15, 20]
#
# # Create the first node
# head = Node(data_list[0])
# current_node = head
#
# # Use a loop to create nodes for the remaining elements
# for data in data_list[1:]:
#     new_node = Node(data)
#     current_node.next = new_node
#     current_node = new_node
#
# # Print the elements of the linked list
# current_node = head
# while current_node is not None:
#     print(current_node.data)
#     current_node = current_node.next
