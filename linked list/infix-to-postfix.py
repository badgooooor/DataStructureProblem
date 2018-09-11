class Stack:
    def __init__(self, list=None):
        if list == None:
            self.items = []
            self.len = 0
        else:
            self.items = list
            self.len = len(list)
    
    def push(self, item):
        self.items.append(item)
        self.len += 1

    def pop(self):
        self.len -= 1
        return self.items.pop()

    def peek(self):
        return self.items[self.size()-1]

    def size(self):
        return self.len

    def isEmpty(self):
        return self.len == 0


def postfix(eq):
    prec = {'*':4, '/':3, '+':2, '-':1}
    s = Stack()
    eq.split()
    r = ''
    for a in eq:
        if a.isalpha() or a.isalnum():
            r += a
        elif a in "+-":
            if s.isEmpty() or s.peek() == '(':
                s.push(a)
        elif a in "*/":
            if s.isEmpty() or s.peek() in "+-(":
                s.push(a)
        elif a == '(':
            s.push(a)
        elif a == ')':
            while s.peek() is not '(':
                r += s.pop()
            s.pop()
        else:
            print("Error")
    
    while not s.isEmpty():
        r += s.pop()
    return r

print(postfix('(a+b)*c-d'))