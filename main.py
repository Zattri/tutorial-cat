
'''
Each cat has:
Name
Breed
Colour

Behaviours:
Feed it
Meow
Hiss
Ignore you
Wash it
Scratch you
Pet it

'''
import random

class cat:
    def __init__(self, name, breed, colour):
        self.name = name
        self.breed = breed
        self.colour = colour

    def petCat(self):
        print("You pet", self.name)
        self.ignoreReaction()

    def washCat(self):
        print("You wash", self.name)
        self.sadReaction()

    def feedCat(self):
        print("You feed", self.name)
        self.happyReaction()

    def entertainCat(self):
        print("You try to entertain", self.name)
        self.randomReaction()

    def randomReaction(self):
        num = random.randint(0,2)

        if (num == 0):
            self.happyReaction()

        elif (num == 1):
            self.ignoreReaction()

        elif (num == 2):
            self.sadReaction()

    def happyReaction(self):
        print(self.name, "is happy")

    def ignoreReaction(self):
        print(self.name, "ignores you")

    def sadReaction(self):
        print(self.name, "is sad")

def main():
    bob = cat("Bob", "Maine coone", ["Black", "White"])
    while (True):
        command = input("What do you want to do with the cat? ")
        if (command == "wash"):
            bob.washCat()

        elif (command == "pet"):
            bob.petCat()

        elif (command == "entertain"):
            bob.entertainCat()

        elif (command == "feed"):
            bob.feedCat()

        else:
            print("Your command was not recognised")


main()