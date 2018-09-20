class Stack:
    def __init__(self, list=None):
        if list is None:
            self.list = []
            self.size = 0
        else:
            self.list = list
            self.size = len(list)

    def __str__(self):
        return 'Stack : ' + str(self.list)

    def push(self, value):
        self.size = self.size + 1
        self.list.append(value)

    def pop(self):
        self.size = self.size - 1
        return self.list.pop()

    def peek(self):
        return self.list(len(self.list))

    def reverse(self):
        # Soft-implement from queue.
        q = []
        while not self.isEmpty():
            q.append(self.pop())
        for num in q:
            self.push(num)
        return q

    def isEmpty(self):
        return self.size == 0
        

l = [c for c in input('input:').split()]
print('l = ', l)

s = Stack(l)
print(s)

s.reverse()

print(s)