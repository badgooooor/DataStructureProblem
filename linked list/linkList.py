 # Simple node and linked list.

# This is a normal good-looking node.
class node:
    def __init__(self, data, next=None):
        if next == None:
            self.data = data
            self.next = None
        else:
            self.data = data
            self.next = next

    def getData(self):
        return self.data

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

# Linked list -- with a dummy list.
class LinkedList:
    def __init__(self, head=None):
        self.dummy = node(None)
        self.head = self.dummy
        if head != None:
            self.dummy.setNext(head)
            self.len = 1
        else:
            self.len = 0

    def __str__(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.getData())
            curr = curr.getNext()
        print(result)

    # insert methods
    def append(self, data):
        new = node(data)
        if self.head == None:
            self.head = new
        else:
            r = self.head
            while r.getNext() != None:
                r = r.getNext()
            r.next = new
        self.len += 1
    
    def addHead(self, data):
        new = node(data)
        new.setNext(self.dummy.getNext())
        self.dummy.setNext(new)
        self.len += 1

    # find methods
    def search(self, data):
        curr = self.head
        count = 0
        while curr:
            if curr.getData() == data:
                return count
            curr = curr.getNext()
            count += 1
        return False

    def before(self, data):
        prev = None
        curr = self.head
        while curr:
            if curr.getData() == data and prev != None:
                return prev.getData()
            prev = curr
            curr = curr.getNext()
        return False
    
    # delete methods
    def remove(self, data):
        prev = None
        curr = self.head
        while curr:
            if curr.getData() == data:
                # Data is at head
                if prev == None:
                    self.head = curr.getNext()
                else:
                    prev.setNext(curr.getNext())
                self.len -= 1
                return True
            prev = curr
            curr = curr.getNext()
        return False

    def isEmpty(self):
        return self.len == 0
        
    def size(self):
        return self.len

line = LinkedList()
print(line.size())
line.append('A')
line.append('B')
line.append('C')
line.addHead('E')
line.__str__()
print(line.before('A'))
print(line.size())
print(line.search('C'))
print(line.search('D'))
line.remove('C')
line.__str__()
