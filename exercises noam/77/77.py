def is_valid(s):

    return len(s) % 2 != 0 and s[0] == s[-1] == s[len(s) // 2]



def check():
    valid = 0
    invalid = 0

    for i in range(3):
        user = input("Enter the string :")
        if is_valid(user):
            valid += 1
        else:
            invalid += 1
    return f"is valid:{valid}, invalid:{invalid}"


print(check())
