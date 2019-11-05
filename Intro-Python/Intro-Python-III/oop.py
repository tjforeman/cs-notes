
# code up an inventory system for a store, the store can have multiple departments.
# each department can hold multiple products. 

# do we need a store type? No
# How many departments <10000
# how man products <1000000
# what departments will there be 
# how much space to store unlimited
# access restrictions none 
# product description name, price, count
# product count? 
# product location isle 
# web/mobile command line
# can a product be in multiple departments maybe later but start with no 
# what kind of reporting? 

# Plan: 

# classes for store, dept, and product

# store contains departments (a 'has-a' relationship)
# departments contain products

class Store: 
    def __init__(self, name): # Contructor
        self.name = name
        self.depts = []

    def __str__(self):
        s= f'store: {self.name}:\n'

        for n , d in enumerate(self.depts, start=1):
            s += f"{n}{d.name}\n"
        return s

    def __repr__(self):
        return f'Store({repr(self.name)})'

    def add_dept(self, dept):
        self.depts.append(dept)
        print(self.depts)

class Dept:
    def __init__(self,name):
        self.name = name
    
    def __str__(self):
        return f'Dept: {self.name}'

    def __repr__(self):
        return f'Dept:({repr(self.name)})'

# in the base class we only want attributes that are common to everything in class
class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count 

# Clothing is a Product
class Clothing(Product):
    def __init__ (self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

# SportingGoods is a Product
class SportingGoods(Product):
    def __init__(self, name, price, count, color):
        super().__init__(name, price, count)
        self.color = color

class Shirt(Clothing):
    def __init__(self, name, price, count, sleeve_length):
        super().__init__(name, price, count)
        self.sleeve_length = sleeve_length

class Shoes(Clothing):
    pass




# s is an object 
s = Store("Tylermart") # instantiate a new instance of a class store

print(s)
s.add_dept(Dept("Hockey"))
s.add_dept(Dept("Produce"))

num = input("enter Dept number: ")

i = int(num) - 1
print(f"\n You selected department: {s.depts[i]}")

t= s 
print(t)

# Demo of "moving around" the deparments since tylers_location is a
# reference to (aka "another name for") s.depts[0] or s.depts[1] ​
# tylers_location = s.depts[0]
# tylers_location.name = "Soccer"
# print(tylers_location)
# ​
# tylers_location = s.depts[1]
# print(tylers_location)
# ​
# print('---')



