class MergeSort:
    def __init__(self, arr):
        self.arr = arr

    def merge_sort(self, arr=None):
        if not arr:
            arr = self.arr
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        left = self.merge_sort(left)
        right = self.merge_sort(right)

        i=j=k=0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1


        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        return arr
    


if __name__ == "__main__":
    unsorted_arr = [5, 2, 1, 7, 6, 8, 3, 4, 9, 0, 10, 7, 14, 13, 11]
    my_sort = MergeSort(unsorted_arr)
    sorted_arr = my_sort.merge_sort()
    print(sorted_arr)
