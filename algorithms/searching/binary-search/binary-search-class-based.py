class BinarySearch:
    def __init__(self,arr) -> None:
        self.arr = arr

    def search(self, target):
        left = 0
        right = len(self.arr) - 1

        while left <= right:
            mid = (left+right) // 2
            if self.arr[mid] == target:
                return mid
            elif self.arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
    
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    target = 4
    binary_search = BinarySearch(arr)
    print(binary_search.search(target))