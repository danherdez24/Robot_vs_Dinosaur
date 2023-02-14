from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.active_weapon = Weapon("Sword", 25)
        self.health = 100

    
        
    
    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print(f'{dinosaur.name} was attacked by {self.name} for {self.active_weapon.attack_power} da1mage, leaving {dinosaur.name} with {dinosaur.health} health remaning')