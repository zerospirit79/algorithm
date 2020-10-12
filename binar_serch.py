def binar_serch(list, item):
    low = 0
    high = len(list) - 1
    i = 0
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            i +=1
            return mid
        if guess > item:
            i += 1
            high = mid - 1
        else:
            i += 1
            low = mid + 1
    return None



my_list = [1, 2, 3, 4, 6, 8, 9, 10, 13, 15, 17, 22, 24, 27, 29, 32, 34]
print (binar_serch(my_list, 15))
