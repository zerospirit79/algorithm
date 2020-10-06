"""
алгоритм неубывающий порядок глава 1
"""

def sort_arr(array):
    length = len(array)
    for j in range(2, length):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = key


arr = []
length = int(input("Введите длину массива:"))

for i in range(0, length):
    element = int(input("arr[" + str(i + 1) + "] = "))
    arr.append(element)
sort_arr(arr)
print(arr)
