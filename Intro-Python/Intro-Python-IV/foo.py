class Lifeform:
    def __init__(self,name):
        self.name = name
        self.age = 0

    def sound(self):
        print("generic animal sound")

class Animal(Lifeform): # Animal is a Lifeform
    pass

class Plant(Lifeform):
    def __init__(self, name, is_tree): # overrides the constructor in Lifeform
        super().__init__(name)
        self.is_tree = is_tree

class Cat(Animal):
    def sound(self):
        print("meow")


l = Lifeform("fred")

print(l.name)

a = Animal("marvin")

print(a.name)

c = Cat('alice')

print(c.name)
c.sound()

p = Plant('tom', False)
print(p.age)
p.age = 12
print(p.age)

