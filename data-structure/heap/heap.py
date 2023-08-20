class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, data):
        self.heap.append(data)
        self.__percolate_up(len(self.heap) - 1)

    def get_min(self):
        if self.heap:
            return self.heap[0]
        return None

    def remove_min(self):
        if len(self.heap) > 1:
            min = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.__min_heapify(0)
            return min
        elif len(self.heap) == 1:
            min = self.heap[0]
            del self.heap[0]
            return min
        else:
            return None

    def __percolate_up(self, index):
        parent = (index - 1) // 2
        if index <= 0:
            return
        elif self.heap[parent] > self.heap[index]:
            tmp = self.heap[parent]
            self.heap[parent] = self.heap[index]
            self.heap[index] = tmp
            self.__percolate_up(parent)

    def __min_heapify(self, index):
        left = (index * 2) + 1
        right = (index * 2) + 2
        smallest = index
        if len(self.heap) > left and self.heap[smallest] > self.heap[left]:
            smallest = left
        if len(self.heap) > right and self.heap[smallest] > self.heap[right]:
            smallest = right
        if smallest != index:
            tmp = self.heap[smallest]
            self.heap[smallest] = self.heap[index]
            self.heap[index] = tmp
            self.__min_heapify(smallest)

    def build_heap(self, arr):
        self.heap = arr
        for i in range(len(arr) - 1, -1, -1):
            self.__min_heapify(i)


heap = Heap()
heap.insert(12)
heap.insert(10)
heap.insert(-10)
heap.insert(100)
print(heap.get_min())
print(heap.remove_min())
print(heap.get_min())
heap.insert(-100)
print(heap.get_min())
print(heap.remove_min())
print(heap.get_min())
heap.build_heap([13, -10, 1000, 1, 2, 3, 4, 5, 6, 7])
print(heap.get_min())
print(heap.remove_min())
