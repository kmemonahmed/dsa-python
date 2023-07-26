def queue_with_list():
    queue = []
    queue.append(1)
    queue.append(2)
    queue.append(3)
    queue.append(4)
    queue.append(5)
    print(queue) # [1, 2, 3, 4, 5]

    queue.pop(0)
    print(queue) # [2, 3, 4, 5]

    queue.pop(0)
    print(queue) # [3, 4, 5]

    queue.pop(0)
    print(queue) # [4, 5]

    queue.pop(0)
    print(queue) # [5]

    queue.pop(0)
    print(queue) # []
    


if __name__ == "__main__":
    queue_with_list()