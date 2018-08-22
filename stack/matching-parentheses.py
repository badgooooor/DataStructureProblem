# Stack class
class Stack:
    def __init__(self, list=None):
        if list == None:
            self.items = []
            self.size = 0
        else:
            self.items = list
            self.size = len(list)

    def push(self, item):
        self.items.append(item)
        self.size += 1
    
    def pop(self):
        self.size -= 1
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]
    
    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

# Parentheses checking method.
def checkParentheses(text):
    pushchar , pullchar = "<({[", ">)}]"
    s = Stack()
    for i in range(len(text)):
        if text[i] in pushchar:
            s.push(text[i])
        elif text[i] in pullchar:
            if s.isEmpty():
                return False
            else:
                op = s.pop()
                cl = pushchar[pullchar.index(text[i])]
                if op != cl:
                    return False
    return s.isEmpty()


# Testing
text = input('Enter the text : ')
print(checkParentheses(text))