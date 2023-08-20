class HeapSort:
    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)
        self.build_heap()

    def build_heap(self):
        for i in range(self.size // 2 - 1, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < self.size and self.arr[left] > self.arr[largest]:
            largest = left
        if right < self.size and self.arr[right] > self.arr[largest]:
            largest = right
        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.heapify(largest)

    def sort(self):
        for i in range(self.size - 1, 0, -1):
            self.arr[0], self.arr[i] = self.arr[i], self.arr[0]
            self.size -= 1
            self.heapify(0)
        return self.arr


arr = [5, 9, 3, 10, 45, 2, 12, 11, 1]
heap_sort = HeapSort(arr)
heap_sort.build_heap()
# print heap
print(heap_sort.arr)
# print sorted array
print(heap_sort.sort())