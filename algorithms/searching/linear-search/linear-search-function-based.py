def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    target = 4
    print(linear_search(arr, target))