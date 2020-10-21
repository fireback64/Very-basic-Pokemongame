import time
import numpy as np
import sys


# Delay printing

# print one character at a time
def delay_print(s):

    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


# Create the class
class Pokemon:

    def __init__(self, name, types, moves, evs, health="==================="):
# Save variables as attributes

        self.name = name
        self.types = types
        self.moves = moves
        self.attack = evs["ATTACK"]
        self.defense = evs["DEFENSE"]
        self.health = health
# Amount of health bars
        self.bars = 20


    def fight (self, pokemon2):
# Allow teo pokemon to fight each other

# Print fight information
        print("-------Pokemon Battle----------")
        print(f"\n{self.name}")
        print("\nTYPE/", self.types)
        print("\nATTACK/", self.attack)
        print("\nDEFENSE/", self.defense)
        print("\nLVL/", 3*(1+np.mean([self.attack, self.defense])))
        print("\nvs")

        print(f"\n{pokemon2.name}")
        print("\nTYPE/", pokemon2.types)
        print("\nATTACK/", pokemon2.attack)
        print("\nDEFENSE/", pokemon2.defense)
        print("\nLVL/", 3 * (1 + np.mean([pokemon2.attack, pokemon2.defense])))


        time.sleep(3)

# Type advantages
        version =["Fire", "Water", "Grass"]

        for i, k in enumerate(version):
            if self.types == k:
# Both are same types:
                if pokemon2.types == k:

                    string_1_attack = "\nIts not very effective..."
                    string_2_attack = "\nIts not very effective..."
# pokemon2 is Stronger
                if pokemon2.types == version[(i+1) % 3]:
                    pokemon2.attack *= 2
                    pokemon2.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    string_1_attack = "\nIts not very effective..."
                    string_2_attack = "\nIts super effective!!!!"
# Pokemon2 is weak
                if pokemon2.types == version[(i+2) % 3]:
                    self.attack *= 2
                    self.defense *= 2
                    pokemon2.attack /= 2
                    pokemon2.defense /= 2
                    string_1_attack = "\nIts super effective!!!!"
                    string_2_attack = "\nIts not very effective..."

# Now fighting
# Continue while pokemon is still alive

        while(self.bars > 0) and (pokemon2.bars > 0):
# print the health of each pokemon
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"\n{pokemon2.name}\t\tHLTH\t{pokemon2.health}\n")

            print(f"\nGo {self.name}! ")
            for i, x in enumerate(self.moves):
                print(f"\n{i+1},", x)
            index = int(input("Pick a move: "))
            delay_print(f"{self.name} used {self.moves[index -1]}!")
            time.sleep(1)
            delay_print(string_1_attack)

# Determine Damage
            pokemon2.bars -= self.attack
            pokemon2.health = ""

# Add back bars plus defense boost
            for j in range(int(pokemon2.bars +.1 * pokemon2.defense)):
                pokemon2.health += "="

            time.sleep(1)

            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"\n{pokemon2.name}\t\tHLTH\t{pokemon2.health}\n")

            time.sleep(.5)
# Check if pokemon 2 fainted after attack from pokemon 1

            if (pokemon2.bars <=0):

                delay_print("\n...." + pokemon2.name + " fainted.")
                break

# pokemon2 turn

            print(f"Go {pokemon2.name}! ")
            for i, x in enumerate(pokemon2.moves):
                print(f"\n{i + 1},", x)
            index = int(input("Pick a move: "))
            delay_print(f"\n{pokemon2.name} used {pokemon2.moves[index - 1]}!")
            time.sleep(1)
            delay_print(string_2_attack)

            # Determine Damage
            self.bars -= pokemon2.attack
            self.health = ""

            # Add back bars plus defense boost
            for j in range(int(self.bars + .1 * self.defense)):
                self.health += "="

            time.sleep(1)

            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"\n{pokemon2.name}\t\tHLTH\t{pokemon2.health}\n")

            time.sleep(.5)
            # Check if pokemon 2 fainted after attack from pokemon 1

            if (self.bars <= 0):
                delay_print("\n...." + self.name + "fainted.")
                money = np.random.choice(5000)
                delay_print(f"\nOpponent paid you ${money}")
                break


#Choose Pokemon
time.sleep(1)
pokemon01_choice = int(input("\nChoose your Pokemon:\n 1(Charizard), \n2(Blastoise) \n3(Venusaur)\n 4(Charmander)\n 5(Squirtle)\n 6(Bulbasaur)\n 7(Charmeleon)\n 8(Wartortle)\n 9(Ivysaur)\n: "))
pokemon02_choice = int(input("\nChoose your Pokemon: \n 1(Charizard), \n2(Blastoise) \n3(Venusaur)\n 4(Charmander)\n 5(Squirtle)\n 6(Bulbasaur)\n 7(Charmeleon)\n 8(Wartortle)\n 9(Ivysaur)\n: "))

# Create pokemon
if __name__ == '__main__':
    Charizard = Pokemon("Charizard", "Fire", ["Flamethrower", "Fly", "Blast Burn", "Fire Punch"], {"ATTACK": 12, "DEFENSE":8})
    Blastoise = Pokemon("Blastoise", "Water", ["Water Gun", "Bubblebeam", "Hydro Pump", "Surf"], {"ATTACK":10, "DEFENSE":10})
    Venusaur = Pokemon("Venusaur", "Grass", ["Vine wip", "Razor leaf", "Earthquake", "Frenzy Plant"], {"ATTACK":8, "DEFENSE":12})

    Charmander = Pokemon("Charmender", "Fire", ["Ember", "Scratch", "Tackle", "Fire Punch"], {"ATTACK" : 4,"DEFENSE":2})
    Squirtle = Pokemon("Squirtle", "Water", ["Bubblebeam", "Tackle", "Headbutt", "Surf"], {"ATTACK": 3, "DEFENSE":4})
    Bulbasaur = Pokemon("Bulbasaur", "Grass", ["Vine Wip", "Razor leaf", "Tackle", "Leech seed"], {"ATTACK" : 2, "DEFENSE" : 4})

    Charmeleon = Pokemon("Charmeleon", "Fire", ["Ember", "Scratch", "Flamethrower", "Fire Punch"], {"ATTACK" : 6, "DEFENSE" : 5})
    Wartortle = Pokemon("Wartortle", "Water", ["Bubblebeam", "Water gun", "Headbutt", "Surf"], {"ATTACK" : 6, "DEFENSE" : 5})
    Ivysaur = Pokemon("Ivysaur\t", "Grass", ["Vine Wip", "Razor Leaf", "Bullet Seed", "Leech Seed"], {"ATTACK":4, "DEFENSE":6})


# Get them to fight each other
    if (pokemon01_choice == 1) and (pokemon02_choice == 1):
        Charizard.fight(Charizard)
    elif(pokemon01_choice == 1) and (pokemon02_choice == 2):
        Charizard.fight(Blastoise)
    elif(pokemon01_choice == 1) and (pokemon02_choice == 3):
        Charizard.fight(Venusaur)
    elif(pokemon01_choice == 1) and (pokemon02_choice == 4):
        Charizard.fight(Charmander)
    elif (pokemon01_choice == 1) and (pokemon02_choice == 5):
        Charizard.fight(Squirtle)
    elif (pokemon01_choice == 1) and (pokemon02_choice == 6):
        Charizard.fight(Bulbasaur)
    elif (pokemon01_choice == 1) and (pokemon02_choice == 7):
        Charizard.fight(Charmeleon)
    elif (pokemon01_choice == 1) and (pokemon02_choice == 8):
        Charizard.fight(Wartortle)
    elif (pokemon01_choice == 1) and (pokemon02_choice == 9):
        Charizard.fight(Ivysaur)

    elif (pokemon01_choice == 2) and (pokemon02_choice == 1):
        Blastoise.fight(Charizard)
    elif (pokemon01_choice == 2) and (pokemon02_choice == 2):
        Blastoise.fight(Blastoise)
    elif (pokemon01_choice == 2) and (pokemon02_choice == 3):
        Blastoise.fight(Venusaur)
    elif (pokemon01_choice == 2) and (pokemon02_choice == 4):
        Blastoise.fight(Charmander)
    elif (pokemon01_choice == 2) and (pokemon02_choice == 5):
        Blastoise.fight(Squirtle)
    elif (pokemon01_choice == 2) and (pokemon02_choice == 6):
        Blastoise.fight(Bulbasaur)
    elif (pokemon01_choice == 2) and (pokemon02_choice == 7):
        Blastoise.fight(Charmeleon)
    elif (pokemon01_choice == 2) and (pokemon02_choice == 8):
        Blastoise.fight(Wartortle)
    elif (pokemon01_choice == 2) and (pokemon02_choice == 9):
        Blastoise.fight(Ivysaur)

    elif (pokemon01_choice == 3) and (pokemon02_choice == 1):
        Venusaur.fight(Charizard)
    elif (pokemon01_choice == 3) and (pokemon02_choice == 2):
        Venusaur.fight(Blastoise)
    elif (pokemon01_choice == 3) and (pokemon02_choice == 3):
        Venusaur.fight(Venusaur)
    elif (pokemon01_choice == 3) and (pokemon02_choice == 4):
        Venusaur.fight(Charmander)
    elif (pokemon01_choice == 3) and (pokemon02_choice == 5):
        Venusaur.fight(Squirtle)
    elif (pokemon01_choice == 3) and (pokemon02_choice == 6):
        Venusaur.fight(Bulbasaur)
    elif (pokemon01_choice == 3) and (pokemon02_choice == 7):
        Venusaur.fight(Charmeleon)
    elif (pokemon01_choice == 3) and (pokemon02_choice == 8):
        Venusaur.fight(Wartortle)
    elif (pokemon01_choice == 3) and (pokemon02_choice == 9):
        Venusaur.fight(Ivysaur)

    elif (pokemon01_choice == 4) and (pokemon02_choice == 1):
        Charmander.fight(Charizard)
    elif (pokemon01_choice == 4) and (pokemon02_choice == 2):
        Charmander.fight(Blastoise)
    elif (pokemon01_choice == 4) and (pokemon02_choice == 3):
        Charmander.fight(Venusaur)
    elif (pokemon01_choice == 4) and (pokemon02_choice == 4):
        Charmander.fight(Charmander)
    elif (pokemon01_choice == 4) and (pokemon02_choice == 5):
        Charmander.fight(Squirtle)
    elif (pokemon01_choice == 4) and (pokemon02_choice == 6):
        Charmander.fight(Bulbasaur)
    elif (pokemon01_choice == 4) and (pokemon02_choice == 7):
        Charmander.fight(Charmeleon)
    elif (pokemon01_choice == 4) and (pokemon02_choice == 8):
        Charmander.fight(Wartortle)
    elif (pokemon01_choice == 4) and (pokemon02_choice == 9):
        Charmander.fight(Ivysaur)

    elif (pokemon01_choice == 5) and (pokemon02_choice == 1):
        Squirtle.fight(Charizard)
    elif (pokemon01_choice == 5) and (pokemon02_choice == 2):
        Squirtle.fight(Venusaur)
    elif (pokemon01_choice == 5) and (pokemon02_choice == 3):
        Squirtle.fight(Venusaur)
    elif (pokemon01_choice == 5) and (pokemon02_choice == 4):
        Squirtle.fight(Charmander)
    elif (pokemon01_choice == 5) and (pokemon02_choice == 5):
        Squirtle.fight(Squirtle)
    elif (pokemon01_choice == 5) and (pokemon02_choice == 6):
        Squirtle.fight(Bulbasaur)
    elif (pokemon01_choice == 5) and (pokemon02_choice == 7):
        Squirtle.fight(Charmeleon)
    elif (pokemon01_choice == 5) and (pokemon02_choice == 8):
        Squirtle.fight(Wartortle)
    elif (pokemon01_choice == 5) and (pokemon02_choice == 9):
        Squirtle.fight(Ivysaur)

    elif (pokemon01_choice == 6) and (pokemon02_choice == 1):
        Bulbasaur.fight(Charizard)
    elif (pokemon01_choice == 6) and (pokemon02_choice == 2):
        Bulbasaur.fight(Blastoise)
    elif (pokemon01_choice == 6) and (pokemon02_choice == 3):
        Bulbasaur.fight(Venusaur)
    elif (pokemon01_choice == 6) and (pokemon02_choice == 4):
        Bulbasaur.fight(Charmander)
    elif (pokemon01_choice == 6) and (pokemon02_choice == 5):
        Bulbasaur.fight(Squirtle)
    elif (pokemon01_choice == 6) and (pokemon02_choice == 6):
        Bulbasaur.fight(Bulbasaur)
    elif (pokemon01_choice == 6) and (pokemon02_choice == 7):
        Bulbasaur.fight(Charmeleon)
    elif (pokemon01_choice == 6) and (pokemon02_choice == 8):
        Bulbasaur.fight(Wartortle)
    elif (pokemon01_choice == 6) and (pokemon02_choice == 9):
        Bulbasaur.fight(Ivysaur)

    elif (pokemon01_choice == 7) and (pokemon02_choice == 1):
        Charmeleon.fight(Charizard)
    elif (pokemon01_choice == 7) and (pokemon02_choice == 2):
        Charmeleon.fight(Blastoise)
    elif (pokemon01_choice == 7) and (pokemon02_choice == 3):
        Charmeleon.fight(Venusaur)
    elif (pokemon01_choice == 7) and (pokemon02_choice == 4):
        Charmeleon.fight(Charmander)
    elif (pokemon01_choice == 7) and (pokemon02_choice == 5):
        Charmeleon.fight(Squirtle)
    elif (pokemon01_choice == 7) and (pokemon02_choice == 6):
        Charmeleon.fight(Bulbasaur)
    elif (pokemon01_choice == 7) and (pokemon02_choice == 7):
        Charmeleon.fight(Charmeleon)
    elif (pokemon01_choice == 7) and (pokemon02_choice == 8):
        Charmeleon.fight(Wartortle)
    elif (pokemon01_choice == 7) and (pokemon02_choice == 9):
        Charmeleon.fight(Ivysaur)

    elif (pokemon01_choice == 8) and (pokemon02_choice == 1):
        Wartortle.fight(Charizard)
    elif (pokemon01_choice == 8) and (pokemon02_choice == 2):
        Wartortle.fight(Blastoise)
    elif (pokemon01_choice == 8) and (pokemon02_choice == 3):
        Wartortle.fight(Venusaur)
    elif (pokemon01_choice == 8) and (pokemon02_choice == 4):
        Wartortle.fight(Charmander)
    elif (pokemon01_choice == 8) and (pokemon02_choice == 5):
        Wartortle.fight(Squirtle)
    elif (pokemon01_choice == 8) and (pokemon02_choice == 6):
        Wartortle.fight(Bulbasaur)
    elif (pokemon01_choice == 8) and (pokemon02_choice == 7):
        Wartortle.fight(Charmeleon)
    elif (pokemon01_choice == 8) and (pokemon02_choice == 8):
        Wartortle.fight(Wartortle)
    elif (pokemon01_choice == 8) and (pokemon02_choice == 9):
        Wartortle.fight(Ivysaur)

    elif (pokemon01_choice == 9) and (pokemon02_choice == 1):
        Ivysaur.fight(Charizard)
    elif (pokemon01_choice == 9) and (pokemon02_choice == 2):
        Ivysaur.fight(Blastoise)
    elif (pokemon01_choice == 9) and (pokemon02_choice == 3):
        Ivysaur.fight(Venusaur)
    elif (pokemon01_choice == 9) and (pokemon02_choice == 4):
        Ivysaur.fight(Charmander)
    elif (pokemon01_choice == 9) and (pokemon02_choice == 5):
        Ivysaur.fight(Squirtle)
    elif (pokemon01_choice == 9) and (pokemon02_choice == 6):
        Ivysaur.fight(Bulbasaur)
    elif (pokemon01_choice == 9) and (pokemon02_choice == 7):
        Ivysaur.fight(Charmeleon)
    elif (pokemon01_choice == 9) and (pokemon02_choice == 8):
        Ivysaur.fight(Wartortle)
    else:
        Ivysaur.fight(Ivysaur)
