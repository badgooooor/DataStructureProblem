# Create linked list with delete repeated data.
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class List:
    def __init__(self, head=None):
        if head is None:
            self.head = None
            self.size = 0
        else:
            self.head = Node(head)
            self.size = 1

    def __str__(self):
        c = self.head
        r = []
        while c:
            r.append(c.data)
            c = c.next
        return 'List :: Size :' + str(self.size) + ' , Data : ' + str(r) 

    def add(self, value):
        new = Node(value)
        self.size = self.size + 1
        if self.head is None:
            self.head = new
        else:
            c = self.head
            while c.next is not None:
                c = c.next
            c.next = new


def createList(l):
    newL = List()
    for item in l:
        newL.add(item)
    return newL

def printList(L):
    print(L.__str__())

def delRepeat(L):
    p = None
    c = L.head
    r = []
    while c:
        if c.data not in r:
            r.append(c.data)
            p = c
            c = c.next
        else:
            L.size = L.size - 1
            p.next = c.next
            c = c.next
    print('Delete repeated data : '+str(r))


data = [c for c in input('Input : ').split()]

li = createList(data)
printList(li)

delRepeat(li)
printList(li)