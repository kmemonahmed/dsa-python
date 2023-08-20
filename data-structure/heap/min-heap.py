class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def insertKey(self, k):
        self.heap.append(k)
        i = len(self.heap) - 1
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = (
                self.heap[self.parent(i)],
                self.heap[i],
            )
            i = self.parent(i)

    def decreaseKey(self, i, new_val):
        self.heap[i] = new_val
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = (
                self.heap[self.parent(i)],
                self.heap[i],
            )
            i = self.parent(i)

    def extractMin(self):
        if len(self.heap) == 0:
            return -1
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.minHeapify(0)
        return root

    def deleteKey(self, i):
        self.decreaseKey(i, float("-inf"))
        self.extractMin()

    def minHeapify(self, i):
        l = 2 * i + 1
        r = 2 * i + 2
        smallest = i
        if l < len(self.heap) and self.heap[l] < self.heap[i]:
            smallest = l
        if r < len(self.heap) and self.heap[r] < self.heap[smallest]:
            smallest = r
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.minHeapify(smallest)

    def buildHeap(self, arr):
        self.heap = arr
        for i in range(len(arr) - 1, -1, -1):
            self.minHeapify(i)



heap = MinHeap()
# build heap
heap.buildHeap([9, 8, 7, 6, 5, 4, 3, 2, 1])
print(heap.heap)