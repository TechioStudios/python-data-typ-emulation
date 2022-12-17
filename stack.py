#stacks:   last-in first-out
#push: add element to top
#pop: remove top element

class Stack():
    def __init__(self):
        self.stack = []
    def push(self,value):
        self.stack.append(value)
    def pop(self):
        try:
            return self.stack.pop()
        except BaseException:
            return "Stack is empty!"
    def peek(self):
        try:
            return self.stack[-1]
        except BaseException:
            return "Stack is empty!"
    def isEmpty(self):
        if self.stack:
            return False
        else:
            return True
    def size(self):
        return len(self.stack)
    def clear(self):
        self.stack = []