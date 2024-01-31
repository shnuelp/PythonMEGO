# # # import random
# # # import re
# # #
# # #
# # # def random_uppercase_letters(s):
# # #     uppercase_letters = re.findall(r"[A-Z]", s)
# # #     if len(uppercase_letters) > 0:
# # #       new_s = "".join(random.choices(uppercase_letters, k=len(s)))
# # #
# # #       return new_s
# # #
# # #
# # # new_s = random_uppercase_letters("cdscvds")
# # # print(new_s)
# #
# # # def star(n):
# # #     if n > 0:
# # #
# # #         star(n - 1)
# # #         print(n * "*")
# # #
# # #
# # # star(5)
# #
# #
# # def is_specific_factorial(num) :
# #   result = 1
# #   i = 1
# #
# #   while result < num:
# #         i += 1
# #         result *= i
# #
# #         if result == num:
# #              print(f"Yes! {i}")
# #         else:
# #             print('No')
# #
# # is_specific_factorial(120)
# # is_specific_factorial(20)
# #
# # # 5
# # # no
#
# def factorization(n):
#     factors = []
#     i = 2
#     while i * i <= n:
#         if n % i:
#             i += 1
#         else:
#             n //= i
#             factors.append(i)
#     if n > 1:
#         factors.append(n)
#     return factors
#
# def perfect_numbers(n):
#     perfects = []
#     for i in range(1, n+1):
#         if sum(factorization(i)) == 2*i:
#             perfects.append(i)
#     return perfects
#
# # Example usage
# n = 10000
# perfects = perfect_numbers(n)
# print("The perfect numbers up to", n, "are:", perfects)
#


# def is_fibonacci(n):
#     if n < 0:
#         return 0
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         a, b = 0, 1
#         while b < n:
#             a, b = b, a + b
#         if b == n:
#             print("is_fibonacci")
#         elif b % n > (b - a) % n:
#             print(b-a)
#         elif b % n < (b + a) % n:
#             print(b)
#         elif b % n < (b - a) % n:
#             print(b)
#         elif b % n > (b + a) % n:
#             print(b+a)
#
#
# number = int(input("Enter a number: "))
# is_fibonacci(number)


def nearest_fibonacci(n):
    if n == 0:
        return 0
    first, second = 0, 1
    third = first + second
    while third <= n:
        first = second
        second = third
        third = first + second
    return second if abs(third - n) >= abs(second - n) else third

number = int(input("Enter a number: "))
print(f"The closest Fibonacci number to {number} is {nearest_fibonacci(number)}")

