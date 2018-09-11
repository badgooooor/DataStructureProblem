class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
    
class DoublyList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def __str__(self):
        cur = self.head
        r = []
        while cur is not None:
            r.append(cur.data)
            cur = cur.next
        print('List :',r)
        print('Size :',self.size())

    def append(self, data):
        new = Node(data)
        if self.head == None:
            self.head = self.tail = new
        else:
            new.prev = self.tail
            new.next = None
            self.tail.next = new
            self.tail = new
        self.len = self.len + 1

    def remove(self, node_value):
        cur = self.head
        while cur is not None:
            if cur.data == node_value:
                if cur.prev is not None:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                else:
                    self.head = cur.next
                    cur.prev = None
                self.len = self.len - 1
            cur = cur.next

    def size(self):
        return self.len

    def isEmpty(self):
        return self.len == 0

l = DoublyList()
l.append(2)
l.append(5)
l.append(7)
l.append(9)
l.append(0)
l.__str__()
l.remove(7)
l.__str__()