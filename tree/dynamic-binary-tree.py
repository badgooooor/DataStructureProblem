class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = None if left is None else self.left
        self.right = None if right is None else self.right


def createTree(root=None):
    if root is None:
        return None
    return Node(root)

def insertNode(root, new):
    if root is None:
        return Node(new)
    else:
        if root.data > new:
            if root.left is None:
                root.left = Node(new)
            else:
                insertNode(root.left, new)
        elif root.data <= new:
            if root.right is None:
                root.right = Node(new)
            else:
                insertNode(root.right, new)
    return root

# Get inorder successor by getting most left node.(for node deletion)
def getSuccessor(node):
    c = node
    while c.left is not None:
        c = c.left
    return c

def deleteNode(root, target):
    if root is None:
        return root
    if root.data > target:
        root.left = deleteNode(root.left, target)
    elif root.data < target:
        root.right = deleteNode(root.right, target)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = getSuccessor(root.right)
        root.data = temp.data
        root.right = deleteNode(root.right, temp.data)
    return root

def searchNode(root, target):
    if root is None or root.data == target:
        return root
    if root.data > target:
        return searchNode(root.left, target)
    elif root.data < target:
        return searchNode(root.right, target)

# Printing tree.
def inOrder(root):
    if root.left:
        inOrder(root.left)
    print(root.data)
    if root.right:
        inOrder(root.right)

def preOrder(root):
    print(root.data)
    if root.left:
        preOrder(root.left)
    if root.right:
        preOrder(root.right)

def postOrder(root):
    if root.left:
        postOrder(root.left)
    if root.right:
        postOrder(root.right)
    print(root.data)

# Print all tree.(inorder)
def printTree(root):
    print('======= Tree =======')
    _printTree(root, 0)
    print()

def _printTree(root, level):
    if root:
        _printTree(root.right, level + 1)
        print(level,' ','   '*level, root.data, sep='')
        _printTree(root.left, level + 1)

# Testing.
l = [14,4,9,7,15,3,18,16,20,5,16,1,2]
r = createTree()

for element in l:
    r = insertNode(r, element)

r = deleteNode(r, 16)
printTree(r)
print(searchNode(r,5))