class InsetionSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        for i in range(1, len(self.arr)):
            item = self.arr[i]
            j = i - 1

            while j >= 0 and self.arr[j] > item:
                self.arr[j+1] = self.arr[j]
                j = j - 1

            self.arr[j+1] = item


unsorted_arr = [5, 2, 1, 7, 6, 8, 3, 4, 9, 0, 10, 7, 14, 14, 16, 13, 11]
insetion_sort = InsetionSort(unsorted_arr)
insetion_sort.sort()
print(insetion_sort.arr)