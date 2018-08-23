# ==== CAESAR CIPHER PROBLEM ====
# Objective :   - Encrypt/decrypt normal/encrypted message.
#               - Add complexity by using set of position numbers.

# Queue class.
class Queue:
    def __init__(self, list=None):
        if list == None:
            self.items = []
            self.len = 0
        else:
            self.items = list
            self.len = len(list)

    def __str__(self):
        return 'Queue : ' +str(self.items)

    def enQueue(self, item):
        self.items.append(item)
        self.len += 1

    def deQueue(self):
        self.len -= 1
        return self.items.pop(0)

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return self.len


# Encrypt/decrypt in each character.
def charEncrypt(char, pos):
    if ord(char) + pos >= ord('z'):
        return chr(int(ord('a')) + int(ord('z') - ord(char)))
    else:
        return chr(ord(char) + pos)

def charDecrypt(char, pos):
    if ord(char) - pos < ord('a'):
        return chr(int(ord('z')) - int(ord(char) - ord('a')))
    else:
        return chr(ord(char) - pos) 

# Test encrypt/decrypt
print(charEncrypt('a',2))
print(charDecrypt('a',2))


# Implement both for encrypt/decrypt messages.
# * Queue is used for storing and getting shifting number.
def encrypt(text, nums):
    seq = Queue(nums)
    result = ""
    for c in text:
        if c != ' ':
            pos = seq.deQueue()      
            seq.enQueue(pos)
            result += charEncrypt(c, pos)
        else:
            result += c
    return result

def decrypt(text, nums):
    seq = Queue(nums)
    result = ""
    for c in text:
        if c != ' ':
            pos = seq.deQueue()
            seq.enQueue(pos)
            result += charDecrypt(c, pos)
        else:
            result += c
    return result


# Testing.
# 1. Checking queue
num = Queue([1,2,3])
print(num.__str__())

# 2. Encrypt/ Decrypt message
print(encrypt('aaaa', [1,2,3]))
print(decrypt('bcdb', [1,2,3]))