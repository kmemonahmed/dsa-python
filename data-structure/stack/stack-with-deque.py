from collections import deque

def stack_with_deque():
    stack = deque()

    stack.append(1)
    stack.append(2)
    stack.append(3)

    print(stack)

    stack.pop()
    print(stack)

    stack.pop()
    print(stack)
    
    stack.pop()
    print(stack)


if __name__ == "__main__":
    stack_with_deque()