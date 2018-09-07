import math

class node:
    def __init__(self, value, next=None):
        if next == None:
            self.value = value
            self.next = None
        else:
            self.value = value
            self.next = next

    def setData(self, value):
        self.value = value

    def getData(self):
        return self.value

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

class List:
    def __init__(self, head = None):
        if head != None:
            self.head = head
            self.len = 1
        else:
            self.head = None
            self.len = 0

    def __str__(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.getData())
            curr = curr.getNext()
        print('List : ', result)
        print('Size : ', self.size())

    def append(self, value):
        new = node(value)
        if self.head == None:
            self.head = new
        else:
            curr = self.head
            while curr.getNext() != None:
                curr = curr.getNext()
            curr.setNext(new)
        self.len = self.len + 1

    def deleteMiddle(self):
        target = math.ceil(self.size() / 2)
        r = 1
        curr = self.head
        prev = None
        if not self.isEmpty():
            if self.size() == 1:
                self.head = None
                self.len = 0
            else:
                while r < target:
                    if prev == None:
                        prev = self.head
                    else:
                        prev = prev.getNext()
                    curr = curr.getNext()
                    r = r + 1
                prev.setNext(curr.getNext())
                self.len = self.len - 1

    def size(self):
        return self.len
    
    def isEmpty(self):
        return self.len == 0


# Test
ll = List()
ll.append(5)
ll.append(4)
ll.append(3)
ll.append(2)
ll.append(1)

ll.__str__()
ll.deleteMiddle()
ll.__str__()