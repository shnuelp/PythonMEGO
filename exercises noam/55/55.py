def num(x, y):
    x2 = x % 10
    y2 = y % 10
    a = x2 == y2
    while x >= 10:
        x // 10
    while y >= 10:
        y // 10
        b = x == y
    return a and b

return x == y and end

# def return_first(n):
#     return n if n < 10 else return_first(n // 10)


# def num(x, y):
#     return return_first(x) == return_first(y) and x % 10 == y % 10
#
#
# print(num(67755, 45))