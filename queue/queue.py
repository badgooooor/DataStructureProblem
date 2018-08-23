class Queue:
    def __init__(self, list=None):
        if list == None:
            self.items = []
            self.len = 0
        else:
            self.items = list
            self.len = len(list)

    def __str__(self):
        return self.items

    def enQueue(self, item):
        self.items.append(item)
        self.len += 1

    def deQueue(self):
        self.len -= 1
        return self.items.pop(0)

    def head(self):
        return self.items[0]

    def tail(self):
        return self.items[self.size()-1]
        
    def isEmpty(self):
        return self.len == 0

    def size(self):
        return self.len

# Test
q = Queue()

q.enQueue(1)            # Add
q.enQueue(2)
q.enQueue(3)
q.enQueue(4)
print(q.size())
print(q.head(), q.tail())
print(q.__str__())

q.deQueue()             # Delete
print(q.__str__())
print(q.head(), q.tail())