class QuickSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        self.quick_sort(0, len(self.arr) - 1)

    def quick_sort(self, low, high):
        if low < high:
            pi = self.partition(low, high)
            self.quick_sort(low, pi - 1)
            self.quick_sort(pi + 1, high)

    def partition(self, low, high):
        pivot = self.arr[high]
        i = low - 1
        for j in range(low, high):
            if self.arr[j] < pivot:
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        self.arr[i + 1], self.arr[high] = self.arr[high], self.arr[i + 1]
        return i + 1
    

arr = [10, 5, 2, 3]
qs = QuickSort(arr)
qs.sort()
print(arr) # [2, 3, 5, 10]
