class BubbleSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        for i in range(0, len(self.arr)):
            for j in range(0, (len(self.arr) - i) -1):
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]


unsorted_arr = [5, 2, 1, 7, 6, 8, 3, 4, 9, 0, 10, 7, 14, 13, 11]
bubble_sort = BubbleSort(unsorted_arr)
bubble_sort.sort()
print(bubble_sort.arr)