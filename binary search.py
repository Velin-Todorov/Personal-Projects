numbers = [9, 0, -1, 89, 10, 11, 4, 5, 6]
numbers.sort()
left = 0
right = len(numbers)
x = 10

"""
here we look for the index of x
"""


def binarySearch(numbers, left, right, x):
    if left > right:  # base case
        return -1

    mid = (left + right) // 2

    if x == numbers[mid]:  # base case
        return mid

    if x < numbers[mid]:
        return binarySearch(numbers, left, mid - 1, x)

    return binarySearch(numbers, mid + 1, right, x)


print(binarySearch(numbers, left, right, x))