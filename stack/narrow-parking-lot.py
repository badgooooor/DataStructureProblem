# Limited stack class
class Stack:
    def __init__(self,maxSize):             # Tweaked the stack from recieve list to size.(prevent exceeded stack.)
        self.items = []
        self.size = 0
        self.maxSize = maxSize

    def __str__(self):
        return self.items

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

    def isFull(self):
        return self.maxSize == self.size

# Parking lot class which is derived from stack class.
class ParkingLot(Stack):
    def __init__(self, maxSize):
        super().__init__(5)
        print('Parking lot with ', self.maxSize,' spaces.')
    
    def carPark(self, car):
        if not super().isFull():
            super().push(car)
            print('Car ', car ,' arrives :: ', self.maxSize - super().getSize() ,'spaces left.')
        else:
            print('the parking lot is full')

    def peekLot(self):
        return super().__str__()

    def carExit(self, car):
        carTemp = []
        temp = 0
        if not car in self.peekLot():
            print('!! No car ', car)
        else:
            print('** Get car ', car,' out')
            while temp != car and not super().isEmpty():
                temp = super().pop()            # Get the car out.
                if temp == car: break
                carTemp.append(temp)
                print('     << Car ', temp,'out')
            carTemp.reverse()
            for c in carTemp:                   # Getting the car back
                super().push(c)
                print('     >> Push back car ', c)


# Testing
lot = ParkingLot(5)             # ! CREATE Parking lot
lot.carPark(1)                  # ? PARKING the car
lot.carPark(2)
lot.carPark(3)
lot.carPark(4)
lot.carPark(5)
lot.carPark(6)                  # ? car is exceeded
print(lot.peekLot())               # Peeking
lot.carExit(3)
print(lot.peekLot())               # Peeking