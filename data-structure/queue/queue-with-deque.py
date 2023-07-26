from collections import deque

def queue_with_dequeue():
    # Initializing a queue
    q = deque()
    
    # Adding elements to a queue
    q.append('a')
    q.append('b')
    q.append('c')
    
    print("Initial queue")
    print(q)
    
    # Removing elements from a queue
    print("\nElements dequeued from the queue")
    print(q.popleft())
    print(q.popleft())
    print(q.popleft())
    
    print("\nQueue after removing elements")
    print(q)
    
    # Uncommenting q.popleft()
    # will raise an IndexError
    # as queue is now empty


if __name__ == "__main__":
    queue_with_dequeue()