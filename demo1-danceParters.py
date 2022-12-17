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



def partners(boyNum,girlNum,NOS):
    result = []
    boys = Queue()
    girls = Queue()
    for i in range(1,boyNum+1):
        boys.add(i)
    for i in range(1,girlNum+1):
        girls.add(i)
    
    for i in range(NOS):
        boy = boys.pop()
        girl = girls.pop()
        boys.add(boy)
        girls.add(girl)
        result.append((boy,girl))
    return result


print(partners(5,2,8))