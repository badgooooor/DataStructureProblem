class Stack:
    def __init__(self, list=None):
        if list == None:
            self.items = []
            self.len = 0
        else:
            self.items = list
            self.len = len(self.items)

    def push(self, value):
        self.items.append(value)
        self.len = self.len + 1

    def pop(self):
        self.len = self.len - 1
        return self.items.pop()

    def peek(self):
        return self.items[self.len - 1]
    def size(self):
        return self.len
    
    def isEmpty(self):
        return self.len == 0


def calculateSpan(price):
    n = len(price)
    S = [None] * n
    S[0] = 1
    s = Stack()
    s.push(0)
    print(s.peek())
    for i in range(1, len(price)):
        while(not s.isEmpty() and price[s.peek()] <= price[i]):
            s.pop()
        S[i] = i + 1 if s.size() <= 0 else i - s.peek()
        s.push(i)
    return S

price = [100, 80, 60, 70, 60, 75, 85]
print(calculateSpan(price))