class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
print("Top element:", stack.peek())  # Output: Top element: 20
print("Popped element:", stack.pop())  # Output: Popped element: 20
print("Is stack empty?", stack.is_empty())  # Output: Is stack empty? False
