class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class List:
    def __init__(self, head=None):
        self.cutPercent = []
        self.rifflePercent = []
        if head == None:
            self.head = None
            self.size = 0
        else:
            self.head = head
            self.size = 1
    
    def __str__(self):
        r = []
        c = self.head
        while c != None:
            r.append(c.data)
            c = c.next
        return r

    def add(self,value):
        new = Node(value)
        self.size = self.size + 1
        if self.head == None:
            self.head = new
        else:
            c = self.head
            while c.next != None:
                c = c.next
            c.next = new

    def remove(self,target):
        c = self.head
        p = None
        while c:
            if c.data == target:
                if p == None:
                    self.head = c.next
                else:
                    p.next = c.next
                self.size = self.size - 1
                return True
            p = c
            c = c.next
        return False   

    def getNode(self, pos):     
        c = self.head
        i = 1
        while i < pos:
            c = c.next
            i = i + 1
        return c

    def bottomUp(self, percent, add=True):
        pos = int(self.size * (percent/100))
        if add:
            self.cutPercent.append(percent)

        c1 = self.getNode(pos)
        c2 = self.getNode(pos+1)
        last = self.getNode(self.size)
        
        last.next = self.head
        self.head = c2
        c1.next = None

        print('Bottom Up ',percent,'% : ',self.__str__())

    def riffle(self, percent, add=True):
        pos = int(self.size * (percent/100))
        if add:
            self.rifflePercent.append(percent)

        a1 = self.head
        a2 = self.getNode(pos)
        b1 = self.getNode(pos+1)
        b2 = self.getNode(self.size)
        a2.next = None
        self.head = b1

        ac1 = a1
        ac2 = a1.next
        bc1 = b1
        bc2 = b1.next

        i = 1
        while i < pos:
            bc1.next = ac1
            ac1.next = bc2
            
            ac1 = ac2
            bc1 = bc2
            ac2 = ac2.next
            bc2 = bc2.next
            i = i + 1
        bc1.next = ac1
        ac1.next = bc2

        print('Shuffle ',percent,'% : ',self.__str__())

    def isEmpty(self):
        return self.size == 0


# Test
l = List()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
l.add(5)
l.add(6)
l.add(7)
l.add(8)
l.add(9)
l.add("Hey!")
print('Original List : ',l.__str__())
l.bottomUp(30)
l.riffle(30)