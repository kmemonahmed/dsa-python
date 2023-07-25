class LinearSearch:
    def __init__(self, arr) -> None:
        self.arr = arr

    def search(self, target):
        for i in range(len(self.arr)):
            if self.arr[i] == target:
                return i
        return -1
        

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    target = 4
    linear_search = LinearSearch(arr)
    print(linear_search.search(target))
