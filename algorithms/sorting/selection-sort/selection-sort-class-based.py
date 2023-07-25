class SelectionSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        for i in range(0, len(self.arr) - 1):
            current_min_index = i
            for j in range(i + 1, len(self.arr)):
                if self.arr[j] < self.arr[current_min_index]:
                    current_min_index = j
            
            if current_min_index != i:
                # traditional swap
                # temp = self.arr[i]
                # self.arr[i] = self.arr[current_min_index]
                # self.arr[current_min_index] = temp

                # python easy swap
                self.arr[i], self.arr[current_min_index] = self.arr[current_min_index], self.arr[i]
    
        return self.arr
    
if __name__ == "__main__":
    unsorted_arr = [5, 2, 1, 7, 6, 8, 3, 4, 9, 0, 10, 7, 14, 13, 11]
    selection_sort = SelectionSort(unsorted_arr)
    selection_sort.sort()
    print(selection_sort.arr)
            