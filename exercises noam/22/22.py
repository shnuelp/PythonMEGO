def pisga(arr1, i):
    if i == 0 or i == arr1[-1]:
        return False

    return arr1[i - 1] < arr1[i] > arr1[i + 1]


def pic(n):
    big = 0
    for i in range(1, len(n) - 1):
        if pisga(arr1, i):
            big += 1
    return big


arr1 = [1, 5, 3, 4, 5, 3]

print(pic(arr1))
print(pisga(arr1,4))
