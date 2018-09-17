class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self, head=None):
        if head is None:
            self.head = None
            self.tail = None
            self.size = 0
        else:
            self.head = Node(head)
            self.tail = self.head
            self.size = 1
    
    # Debug
    def __str__(self):
        r = []
        c = self.head
        while c:
            r.append(c.data)
            c = c.next
        print('Stack : ',r)
        print('Size  : ',self.size)

    def push(self, value):
        new = Node(value)
        self.size = self.size + 1
        if self.head == None:
            self.head = new
            self.tail = new
        elif self.head == self.tail:
            self.tail = new
            self.head.next = self.tail
        else:
            self.tail.next = new
            self.tail = new

    def peek(self):
        return self.tail.data

    def pop(self):
        c = self.head
        while c.next != self.tail:
            c = c.next
        data = self.tail.data
        self.tail = c
        c.next = None
        self.size = self.size - 1
        return data

    def isEmpty(self):
        return self.size == 0
    

q = Stack()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.__str__()
print(q.pop())
q.__str__()
print(q.peek())