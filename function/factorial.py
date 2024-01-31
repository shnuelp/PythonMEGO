# def tax(selery):
#     a = 7010 * 0.9
#     b = a + abs(selery - 7011) * 0.86
#     c = b + abs(selery - 10061) * 0.8
#     d = c + abs(selery - 16151) * 0.69
#     e = d + abs(selery - 22441) * 0.65
#     f = e + abs(selery - 46691) * 0.53
#     g = f + abs(selery - 60131) * 0.50
#
#     if selery <= 7010:
#         return selery * 0.9
#     elif 10060 >= selery >= 7011:
#         return b
#     elif 16150 >= selery >= 10061:
#         return c
#     elif 22440 >= selery >= 16151:
#         return d
#     elif 46690 >= selery >= 22441:
#         return e
#     elif 60130 >= selery >= 46691:
#         return f
#     else:
#         return g
#
#
# print(tax(20000))

def calculate_tax(salary):
    if salary <= 7010:
        return salary * 0.9
    elif 7011 <= salary <= 10060:
        return 7010 * 0.9 + (salary - 7010) * 0.86
    elif 10061 <= salary <= 16151:
        return 7010 * 0.9 + 3050 * 0.86 + (salary - 10060) * 0.8
    elif 16151 <= salary <= 22440:
        return 7010 * 0.9 + 3050 * 0.86 + 6090 * 0.8 + (salary - 16150) * 0.69
    elif 22441 <= salary <= 46690:
        return 7010 * 0.9 + 3050 * 0.86 + 6090 * 0.8 + 6290 * 0.69 + (salary - 22440) * 0.65
    elif 46691 <= salary <= 60130:
        return 7010 * 0.9 + 3050 * 0.86 + 6090 * 0.8 + 6290 * 0.69 + 24250 * 0.65 + (salary - 46690) * 0.53
    else:
        return 7010 * 0.9 + 3050 * 0.86 + 6090 * 0.8 + 6290 * 0.69 + 24250 * 0.65 + 13440 * 0.53 + (salary - 60130) * 0.5

print(calculate_tax(80000))

