# def f(i):
#     if i == 0:
#         return 0
#     if i == 1:
#         return 1
#     return f(i - 2) + f(i - 1)
#
#
# a = f(6)
# print(a)
#
#
# def productFib(prod):
#     num1 = 0
#     num2 = 1
#     nums_prod = num1 * num2
#
#     while nums_prod < prod:
#         num2 = num1 + num2
#         num1 = num2 - num1
#         nums_prod = num1 * num2
#
#     return [num1, num2, nums_prod == prod]  # Return statement outside the loop
# print(productFib(273))
# ↑
# nums_to_check = [144, 1000, 1870, 4128288, 5666, 273]
# for num in nums_to_check:
#     n1, n2, ans = productFib(num)
#     opr = ' == ' if ans else ' != '
# print(f'{n1} x {n2} = {n1 * n2} {opr} {num}')
#
#
# def productFib(prod):
#     a, b = 0, 1
#     while prod > a + b:
#         a, b = b, a + b
#     return [a, b, prod == a + b]
# print(productFib(273))
#
# def is_fibonacci(n):
#     if n < 0:
#         return False
#     elif n == 0 or n == 1:
#         return True
#     else:
#         a, b = 0, 1
#         while b < n:
#             a, b = b, a + b
#         return b == n
#
#
# number = int(input("Enter a number: "))
# if is_fibonacci(number):
#     print(f"{number} is a Fibonacci number.")
# else:
#     print(f"{number} is not a Fibonacci number.")

def fibonacci_closest(n):
    fib_a, fib_b = 0, 1

    while fib_b < n:
        # similar to: fib_a, fib_b = fib_b, fib_a + fib_b
        temp = fib_a
        fib_a = fib_b
        fib_b = temp + fib_b

    # find the closest Fibo. num.
    diff_a = abs(n - fib_a)  # difference between n and fib_a
    diff_b = abs(n - fib_b)  # difference between n and fib_b

    if diff_a < diff_b:
        closest_number = fib_a
    else:
        closest_number = fib_b

    return closest_number


user_input = int(input("Enter a natural number >>> "))
result = fibonacci_closest(user_input)
print("The closest Fibonacci number to", user_input, "is", result)