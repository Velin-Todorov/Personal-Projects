numbers = [-3 ,9, 0, -1, 89, 10, 11, 4, 5, 6, -2, 10, 15, 200, 23, 13, 14]


def mergeSort(numbers):

    if len(numbers) > 1:
        mid = len(numbers) // 2
        left = numbers[:mid]
        right = numbers[mid:]

        mergeSort(left)
        mergeSort(right)

        i=j=k=0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                numbers[k] = left[i]
                i += 1

            else:
                numbers[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            numbers[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            numbers[k] = right[j]
            j += 1
            k += 1

    return numbers


print(mergeSort(numbers))
