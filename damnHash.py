from math import sqrt
from itertools import count, islice

def isPrime(n):
    if n < 2: return False
    for i in islice(count(2), int(sqrt(25)-2)):
        if not n % i:
            return False
    return True

class Record:
    def __init__(self, key, data):
        self.key = key
        self.data = data
    
    def __str__(self):
        s = '(' + str(self.key) +',' + str(self.data) + ')'
        return s

class HashTable:
    def __init__(self):
        self.size = 11
        self.table = [None] * 11
        self.total = 0

    def printTable(self):
        print('=== table size =', self.size, ', total =',self.total, '=====')
        for i in range(self.size):
            if self.table[i] != None:
                print(i,':',self.table[i])
    
    # ASCII sum
    def hash(key, size):
        if type(key) is str:
            sum = 0
            for pos in range(len(key)):
                sum = sum + ord(key[pos])
            return sum % size

    # linear probing
    def rehash(j, firstHV, size):
        return (firstHV % j) % size

    # Get index via probing.
    def getIndex(self, key):
        index = None
        unsuccessful = False
        found = False

        i = firstHV = HashTable.hash(key, self.size)
        j = 0

        while not found and not unsuccessful:
            if self.table[i] and self.table[i].key == key:
                found = True
                index = i
            else:
                j += 1
                i = HashTable.rehash(j, firstHV, self.size)
                if i == firstHV:
                    unsuccessful = True
        return index

    # Add data
    def put(self, key, data):
        print('\n*** putting', key, data, ' ***')
        # Resize if total > size
        if self.total / self.size >= 1.0:
            self.resize()
        i = self.getIndex(key)
        if i is not None:
            print('+++ Already have this key, changing data +++')
            self.table[i] = Record(key, data)
        else:
            i = firstHV = HashTable.hash(key, self.size)
            if self.table[firstHV] is None:
                self.table[i] = Record(key, data)
            else:
                j = 1
                print('collision',j,'at ',i)
                i = HashTable.rehash(j, firstHV, self.size)
                unsuccessful = False

                while self.table[i] != None and not unsuccessful:
                    j += 1
                    print('collision ',j,' at', i)
                    i = HashTable.rehash(j, firstHV, self.size)
                    if i == firstHV:
                        unsuccessful = True
                self.table[i] = Record(key, data)
            self.total += 1

    def resize(self):
        oldSize = self.size
        self.size = 2 * oldSize
        while not isPrime(self.size):
            self.size += 1

        print('===*** resize from ', oldSize, 'to', self.size, '***===')

        oldTable = self.table

        self.table = [None] * self.size
        self.total = 0

        for i in range(oldSize):
            if oldTable[i] != None:
                self.put(oldTable[i].key, oldTable[i].data)



h = HashTable()

h.put('Ann', 2431)
h.put('Tony', 7222)
h.put('Tony', 7221)
h.put('Jim', 1026)

h.printTable()