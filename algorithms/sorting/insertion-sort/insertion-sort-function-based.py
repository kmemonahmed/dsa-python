def insertion_sort(arr):
    for i in range(1, len(arr)):
        item = arr[i]
        j =  i - 1

        while j >= 0 and arr[j] > item:
            arr[j+1] = arr[j]
            j = j - 1

        arr[j+1] = item

    return (arr)

if __name__ == "__main__":
    unsorted_arr = [5, 2, 1, 7, 6, 8, 3, 4, 9, 0, 10, 7, 14, 14, 16, 13, 11]
    sorted_arr = insertion_sort(unsorted_arr)
    print(sorted_arr)