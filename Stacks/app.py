# LIFO
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        return self.stack.append(value)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def size(self):
        return len(self.stack)
    def is_empty(self):
        return len(self.stack)
first_stack = Stack()
first_stack.push(1)
first_stack.push(2)
first_stack.push(3)
# first_stack.pop()
# first_stack.peek()
print(first_stack.size())


# print(first_stack.peek())
print(first_stack.stack)




    