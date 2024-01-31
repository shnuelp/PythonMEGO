def bubblr_sort(arr):


    length = len(arr)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90, 1, 18, 100, 2]
bubblr_sort(arr)
print(arr)


def nummax(arr):
    length = len(arr)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]
nummax(arr)
b = "".join(str(i) for i in arr)
print(b)

