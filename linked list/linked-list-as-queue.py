class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self,head=None):
        if head is None:
            self.head = None
            self.tail = None
            self.size = 0
        else:
            self.head = head
            self.tail = self.head
            self.size = 1

    def __str__(self):
        r = []
        c = self.head
        while c:
            r.append(c.data)
            c = c.next
        print('Queue : ', r)
        print('Size  : ', self.size)

    def enQ(self, value):
        new = Node(value)
        self.size = self.size + 1
        if self.head == None:
            self.head = new
            self.tail = self.head
        elif self.head == self.tail:
            self.tail = new
            self.head.next = self.tail
        else:
            self.tail.next = new
            self.tail = new

    def deQ(self):
        if not self.isEmpty():
            data = self.head.data
            self.head = self.head.next
            self.size = self.size - 1
            return data
        else:
            return False

    def peek(self):
        return self.head.data

    def isEmpty(self):
        return self.size == 0


q = Queue()
q.enQ(1)
q.enQ(2)
q.enQ(3)
q.enQ(4)
q.enQ(5)
print(q.peek())
q.__str__()
print(q.deQ())
print(q.deQ())
q.__str__()