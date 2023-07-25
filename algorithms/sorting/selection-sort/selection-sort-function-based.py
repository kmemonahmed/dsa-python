def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        current_min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[current_min_index]:
                current_min_index = j
        
        if current_min_index != i:
            # traditional swap
            # temp = arr[i]
            # arr[i] = arr[current_min_index]
            # arr[current_min_index] = temp

            # python easy swap
            arr[i], arr[current_min_index] = arr[current_min_index], arr[i]

    return arr

if __name__ == "__main__":
    unsorted_arr = [5, 2, 1, 7, 6, 8, 3, 4, 9, 0, 10, 7, 14, 13, 11]
    sorted_arr = selection_sort(unsorted_arr)
    print(sorted_arr)
            