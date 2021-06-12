
import re
import random
import numpy as np

# https://github.com/russs123/Battle/blob/main/battle.py


diceInput = input("Roll: ")

# Stats = [HP, AC, Attack, Damage, Number of Attacks, ]

PC_AC = 14
PC_Attack = "1d20 + 6"
PC_Damage = "1d12 + 3"

NPC_AC = 16
NPC_Attack = "1d20 + 6"
NPC_Damage = "2d6 + 2"

attack = False
current_fighter = 1
total_fighters = 2
gameOver = 0


def DiceRoll(diceInput):
    total = 0
    rollNumbers = re.findall('[0-9]+', diceInput)
    print(rollNumbers)

    # diceNum = re.sub("[^0-9]","",diceSize)
    for i in range(int(rollNumbers[0])):
        diceResult = random.randint(1, int(rollNumbers[1]))
        print("roll number " + str(i) + " is " + str(diceResult))
        total = total + diceResult

    if len(rollNumbers) > 2:
        diceBonus = int(rollNumbers[2])
    else:
        diceBonus = 0

    return total + diceBonus


class Martial:
    def __init__(self, name = '', AC, MaxHP, Attack, Damage):
        self.name = name
        self.AC = AC
        self.MaxHP = MaxHP
        self.HP = MaxHP
        self.Attack = Attack
        self.Damage = Damage
        self.alive = True

        def attack(self, target):
            if DiceRoll(self.Attack) >= target.AC:
                target.HP -= Damage
                print("Hit")

            if target.HP < 1:
                target.HP = 0
                target.alive = False

Player = Martial("Twang", 14, 71, 1d20+9, 1d12+5)
Bandit_1 = Martial("Bandit 1", 12, 11, 1d20+3, 1d6+1)

enemy_list = []
enemy_list.append(Bandit_1)

run = True
while run:
    
    if gameOver == 0:

        # Player Action
        if Player.alive:
            if current_fighter == 1:

                action_cooldown += 1

                if action_cooldown >= action_


print("The result is " + str(DiceRoll(diceInput)))