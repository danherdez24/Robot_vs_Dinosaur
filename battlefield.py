from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.dinosaur = Dinosaur("Spike", 25)
        self.robot = Robot("Rumba")

    def run_game(self):
        self.display_welcome()
        self.battle_phase()


    def display_welcome(self):
        print('\nWelcome to an epic battle for the ages!\nOnly one side can win!\n')

    def battle_phase(self):
        #2 after testing both attack function try adding a while loop here
        while self.robot.health > 0 and self.dinosaur.health > 0:

            self.robot.attack(self.dinosaur)
        #1 setup dinosaur attack method and test it here
            if self.dinosaur.health > 0:
                self.dinosaur.attack(self.robot)


    def display_winner(self):
        if self.dinosaur.health > 0:
            print(f'{self.dinosaur.name} is the winner of the war!')
        else:   
            print(f'{self.robot.name} is the winner of the war!')