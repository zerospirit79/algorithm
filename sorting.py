def findSmilest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmilest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print(selectionSort([33, 23, 25, 24, 45, 65, 56, 1, 3, 99, 32, 43, 44, 45]))
