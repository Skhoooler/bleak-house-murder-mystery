################################################
# Suspects Class
# 
# This contains all of the information about
# the suspects, including murder weapons,
# scenarios and motivations
################################################
import random

class Suspects:
    def __init__(self):
        # Set up suspects
        self.dedlock = _Dedlock()
        self.george = _George()
        self.smallweed = _Smallweed()
        self.hortense = _Hortense()
        self.esther = _Esther()
        self.suspects = [self.dedlock, self.george, self.smallweed, self.hortense, self.esther]
        
        # Set murderer
        self.murderer = self.suspects[random.randint(0, len(self.suspects) - 1)]

        # Set murder weapon
        self.weapons = [
            "with a knife", 
            "with a gun", 
            "via battery", 
            "by exposure to the elements",
            "by being shoved out of a window" ]
        if (self.murderer == self.smallweed):
            self.weapon = "with a cushion of some kind"
        else:
            self.weapon = self.weapons[random.randint(0, len(self.weapons) - 1)]
        
        # Add clues
        if (self.murderer == self.dedlock):
            self.clues = [
                "A person with a somewhat larger figure was seen fleeing the scene of the crime into the night",
                "Footprints in the snow suggest this person was fleeing in the direction of Chesney Wold",
            ]
        if (self.murderer == self.hortense):
            self.clues = [
                "A person with a smaller figure was seen fleeing the scene of the crime into the night",
                "Footprints in the snow suggest this person was fleeing in the direction of Chesney Wold",
            ]
        if (self.murderer == self.esther):
            self.clues = [
                "A person with a smaller figure was seen fleeing the scene of the crime into the night",
                "Footprints in the snow suggest this person was fleeing in the direction of Bleak House",
            ]
        if (self.murderer == self.george):
            self.clues = [
                "A person with a somewhat larger figure was seen fleeing the scene of the crime into the night",
                "Footprints in the snow suggest this person was fleeing in the direction of Bleak House",
            ]
        if (self.murderer == self.smallweed):
            self.clues = [
                "Person prints in the snow suggest this person was hobbling around slowly and in no particular direction"
                "Mr Tulkinghorn was apparantly killed by a cushion? I'm not sure how that happened...",
                "Some townsfolk heard the suspect, a decrepit old man, muttering to himself about his money as he made his way home",
            ]
    

class _Dedlock:
    name = "Lady Dedlock"
    greeting = "I could have never done this! There is definitely no \nreason for me to want to wish death on poor Mr. Tulkinghorn!"
    
    def question(self):
        print(self.greeting)
        pass

class _George:
    name = "Mr. George"
    greeting = "I had my disagreements with Tulkinghorn, but I am an honest person, and could never had murdered him"
    
    def question(self):
        print(self.greeting)
        pass

class _Smallweed:
    name = "Grandfather Smallweed"
    greeting = "Bah get off my lawn. How could I have possibly killed anyone"
    
    def question(self):
        print(self.greeting)
        pass

class _Hortense:
    name = "Mademoiselle Hortense"
    greeting = "Tulkinghorn had many enemies, not in the least of which was the tretcherous Lady Dedlock, why not ask her about the matter?"

    def question(self):
        print(self.greeting)
        pass

class _Esther:
    name = "Esther"
    greeting = "I'm so sorry, but I didn't do it! I could never harm anyone!"

    def question(self):
        print(self.greeting)
        pass