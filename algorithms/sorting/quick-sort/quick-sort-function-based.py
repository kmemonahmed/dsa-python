def quick_sort(array):
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
        return quick_sort(less) + [pivot] + quick_sort(greater)
    

print(quick_sort([10, 5, 2, 3])) # [2, 3, 5, 10]
print(quick_sort([10, 5, 2, 3, 1, 7, 6, 4, 8, 9])) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(quick_sort([10, 5, 2, 3, 1, 7, 6, 4, 8, 9, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9])) # [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

