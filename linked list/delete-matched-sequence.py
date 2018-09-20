class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def createListWithoutFuckingClass(l):
    head = Node('dummy')
    tmp = head
    while l != []:
        tmp.next = Node(l.pop(0))
        tmp = tmp.next
    return head

def printThatFuckingLinkedList(l):
    curr = l.next
    r = []
    while curr != None:
        r.append(curr.data)
        curr = curr.next
    print('Linked list : ', r)

def deleteSequenceOfNodeThatFuckingTheSameAsTheseDamnString(h, s):
    prev = h
    curr = prev.next
    frontC = prev
    while curr is not None:
        while curr is not None and curr.data == s[0]:
            equal = True
            for char in s:
                if curr.data is None:
                    equal = False
                    break
                if curr.data != char:
                    equal = False
                    break
                else:
                    curr = curr.next
                    frontC = frontC.next
            if equal:
                prev.next = curr
            else:
                prev = frontC
        prev = curr
        if curr != None:
            curr = curr.next
            frontC = frontC.next


ls = ['hellohhello!!hello','hellhhello!!hello','hellhhel!!hello', 'hhelloello']
s = 'hello'
for string in ls:
    l = [c for c in string]
    print('l = ', l)

    h = createListWithoutFuckingClass(l)
    printThatFuckingLinkedList(h)
    deleteSequenceOfNodeThatFuckingTheSameAsTheseDamnString(h,s)

    printThatFuckingLinkedList(h)