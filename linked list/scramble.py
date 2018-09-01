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

# Linked list.
class LinkedList:
    def __init__(self, head=None):
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
        return result

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

    def searchfromPos(self, target):
        curr = self.head
        pos = 1
        if target > self.size():
            return False
        else:
            while pos < target:
                curr = curr.getNext()
                pos += 1
            return curr

    def before(self, data):
        prev = None
        curr = self.head
        while curr:
            if curr.getData() == data and prev != None:
                return prev
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

    def setHead(self, node):
        self.head = node

    # size
    def isEmpty(self):
        return self.len == 0
        
    def size(self):
        return self.len


class Sentence(LinkedList):
    def __init__(self, data):
        self.cutPercent = []
        self.rifflePercent = []
        super().__init__()
        for word in data.split(" "):
            super().append(word)
    
    def cut(self, percent):
        self.cutPercent.append(percent)
        cutPos = int(super().size() * (percent / 100))
        lowestCut = super().searchfromPos(cutPos)
        lowestTwo = super().before(lowestCut.getData())
        afterCut = super().searchfromPos(cutPos + 1)
        tail = super().searchfromPos(super().size())
        head = super().searchfromPos(1)
        
        # Bottom-up
        tail.setNext(head)
        super().setHead(afterCut)
        lowestCut.setNext(None)
        print("Bottom Up " ,str(percent), "% :" , super().__str__())

    def percentCut(self):
        return self.cutPercent.__str__()

    def deCutAll(self):
        print("-- De-cut -------------------------------------")
        for x in reversed(self.cutPercent):
            self.cut(x)
            self.cutPercent.remove(x)
        self.cutPercent = []
    
    def riffle(self, percent):
        print("Riffle ",str(percent),"% :", super().__str__())


text = Sentence("Transquily Base : Hotel and Casino .")
print(text.__str__())
print(text.size())
text.cut(50)
text.cut(40)
text.cut(30)
print(text.deCutAll())
text.riffle(50)