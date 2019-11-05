# Items
# Weapons 
# Enemies 
# rooms 

# potion, books, armour, weapon is-a -> item

# orc is-a enemy 

class Enemy:
    def __init__(self, mean, health, attackpts):
        pass

class Orc(Enemy):
    pass

class Kobold(Enemy):
    pass

class GiantSquid(Enemy):
    def __init__(self,swim_speed):
        pass