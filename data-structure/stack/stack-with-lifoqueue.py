from queue import LifoQueue

def stack_with_lifoqueue():
    stack = LifoQueue(maxsize=3)

    print(stack.qsize())
    
    stack.put('a')
    stack.put('b')
    stack.put('c')
    
    print("Full: ", stack.full())
    print("Size: ", stack.qsize())
    
    print(stack.get())
    print(stack.get())
    print(stack.get())
    
    print("Empty: ", stack.empty())


if __name__ == "__main__":
    stack_with_lifoqueue()