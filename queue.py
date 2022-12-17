#queue: first-in first-out
#Also known as a FIFO
class Queue():
    def __init__(self):
        self.queue = []
    def add(self,item):
        self.queue.append(item)
    def pop(self):
        if self.queue:
            tmp = self.queue[0]
            del self.queue[0]
            return tmp
        else:
            return "Queue is empty!"
    def peek(self):
        if self.queue:
            return self.queue[0]
        else:
            return "Queue is empty!"
    def isEmpty(self):
        if self.queue:
            return False
        else:
            return True
    def size(self):
        return len(self.queue)
    def clear(self):
        self.queue = []