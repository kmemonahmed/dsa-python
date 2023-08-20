def quick_sort_2(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = []
        greater = []
        for i in array[1:]:
            if i <= pivot:
                less.append(i)
            else:
                greater.append(i)
        return quick_sort_2(less) + [pivot] + quick_sort_2(greater)
    

print(quick_sort_2([10, 5, 2, 3])) # [2, 3, 5, 10]
print(quick_sort_2([10, 5, 2, 3, 1, 7, 6, 4, 8, 9])) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(quick_sort_2([10, 5, 2, 3, 1, 7, 6, 4, 8, 9, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9])) # [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

arr = [10, 5, 2, 3]
quick_sort(arr, 0, len(arr) - 1)
print(arr) # [2, 3, 5, 10]


