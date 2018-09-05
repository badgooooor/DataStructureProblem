class Stack:
    def __init__(self, list=None):
        if list is None:
            self.list = []
            self.s = 0
        else:
            self.list = list
            self.s = len(self.list)

    def __str__(self):
        print("Stack :", self.list, "with size of ", self.s)
    
    def push(self, value):
        self.list.append(value)
        self.s = self.s + 1

    def pop(self):
        self.s = self.s - 1
        return self.list.pop()

    def peek(self):
        return self.list[self.s - 1]

    def size(self):
        return self.s

    def isEmpty(self):
        return self.s == 0

def nextGreaterElement(num):
    stack = Stack()
    stack.push(num[0])
    for n in num:
        next = n
        if stack.isEmpty():
            stack.push(n)
        else:
            popped = stack.pop()
            while popped < next:
                print(popped, '--' , next)
                if stack.isEmpty():
                    break
                popped = stack.pop()
            
            if popped > next:
                stack.push(popped)
        stack.push(next)

    while not stack.isEmpty():
        popped = stack.pop()
        next = -1
        print(popped, '--' , next)


# Test
num = [11, 13, 21, 3]
nextGreaterElement(num)