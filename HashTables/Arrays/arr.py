class DynamicArray:
    def __init__ (self,capacity=0):
        self.count = 0
        self.capacity = capacity
        self.storage = [None] * self.capacity # allocate memory 


    def insert (self, index, value):
        if self.count >= self.capacity:
            self.double_size()
            # make array resize
            # print('Error: array is full')
            # return
        # Shift everything at index to the right 
        if index > self.count:
            print('Error: out of range')
            return

        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i-1]

        self.storage[index] = value
        self.count +=1

    def delete(self,index):
        if index>= self.count:
            print('Error: out of range')
            return 

        # Shift everything to the left
        for i in range(index, self.count -1, 1):
            self.storage[i] = self.storage[i + 1]

        self.count -= 1 

    def append(self, value):
        self.insert(self.count, value)
    
    def prepend(self,value):
        self.insert(0,value)

    def double_size(self):
        self.capacity += 2
        new_storage = [None] * self.capacity

        for i in range(self.count):
            new_storage[i] = self.storage[i]

        self.storage = new_storage


myArray = DynamicArray(3)
myArray.append(5)
# myArray.delete(0)
myArray.prepend(4)

print(myArray.storage)

myArray.insert(2,3)

print(myArray.storage)

myArray.delete(2)

print(myArray.storage)

myArray.insert(2,7)

print(myArray.storage)

myArray.append(6)

print(myArray.storage)