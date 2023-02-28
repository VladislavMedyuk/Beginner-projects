from random import randint


def binary_search(list, value):
    mid = len(list) // 2
    low = 0
    high = len(list) - 1

    while list[mid] != value and low <= high:
        if value > list[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if low > high:
        print("No value")
    else:
        print(f"ID = {mid}")
    return mid


list = []
for i in range(10):
    list.append(randint(1, 50))
list.sort()
print(list)

value = int(input())

binary_search(list, value)
