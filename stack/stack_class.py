class Stack:
    def __init__(self, list=None):
        if list == None:
            self.items = []
            self.size = 0
        else:
            self.items = list
            self.size = len(list)
    
    def push(self, item):
        self.items.append(item)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0
