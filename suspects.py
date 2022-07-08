################################################
# Suspects Class
# 
# This contains all of the information about
# the suspects, including murder weapons,
# scenarios and motivations
################################################
import random
from select import select
import time

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

    murdererResponses = ["I just took a small stroll around Chesney Wold.", "He is Sir Leicester Dedlock's lawyer, and nothing more to me.", "My secrets are mine and mine alone."]
    innocentResponses = ["I took a moonlit stroll to be alone with my thoughts.", "He is not a friend. Although he is Sir Leicester Dedlock's lawyer,\n he has attempted to extort me because of my past. I would have never killed him though!", "Mr Tulkinghorn is mechanically faithful without attachment, and very jealous of the profit,\n privilege, and reputation of being master of the mysteries of great houses. My house is no exception.\n Even so, a murderer I am not."]

    accused = "\"I am resolved. I have long outbidden folly with folly, pride with pride, scorn with scorn,\n insolence with insolence, and have outlived many vanities with many more. \nI will outlive this danger, and outdie it, if I can.\" - Lady Dedlock"
    
    def introduction(self):
        print("####################################")
        print("#           Lady Dedlock           #")
        print("####################################")
        print(self.greeting)
        print()
        time.sleep(1)

    def question(self, isGuilty):
        self.introduction()

        done = False
        while not done:
            print("1 - Where were you the night Mr. Tulkinghorn was murdered?")
            print("2 - What was your relationship with Mr. Tulkinghorn like, prior to his murder?")
            print("3 - I understand that he was hot on the trail of learning some of your secrets. Tell me about that.")
            print("4 - No further questions.")
            print()

            try:
                selection = int(input("What would you like to ask Lady Dedlock? "))
                print()

                if (selection == 4):
                    print("Right, back to the others.")
                    done = True
                    break

                if (isGuilty == True):
                    print(self.murdererResponses[selection - 1])
                    print()
                    time.sleep(1)
                else:
                    print(self.innocentResponses[selection - 1])
                    print()
                    time.sleep(1)

                done = False

                continue 

            except:
                print("Sorry, we could not understand you.\n")
                continue

        return

class _George:
    name = "Mr. George"
    greeting = "I had my disagreements with Tulkinghorn, but I am an honest person, and would never had murdered him"

    murdererResponses = ["I had a late night working in my shooting gallery, to try to pay off my debt to Smallweed.", "I'm not sure. I've never talked to the man.", "My quarrel was with the snake Smallweed, not with Mr Tulkinghorn. I paid and paid and paid,\n but he would still destroy my buisness."]
    innocentResponses = ["I was there at Tulkinghorn's home, but I didn't do it!", "I confess I did not know Mr. Tulkinghorn very well. He was my lender's lawyer", "Well, the gallery don't quite do what was expected of it, and it's not - in short, it's not the Mint. \nMr Tulkinghorn was just offering to help me with some payments in exchange for some documents."]
    
    accused = "\"I am as innocent of this charge as yourselves; what has been stated agaisnt me in the way of facts,\nis perfectly true; I know no more about it.\" - Mr. George"

    def introduction(self):
        print("####################################")
        print("#            Mr. George            #")
        print("####################################")
        print(self.greeting)
        print()
        time.sleep(1)
    
    def question(self, isGuilty):
        self.introduction()

        done = False
        while not done:
            print("1 - Where were you the night Mr. Tulkinghorn was murdered?")
            print("2 - What was your relationship with Mr. Tulkinghorn like, prior to his murder?")
            print("3 - Tell me about the letter Mr. Tulkinghorn sent you just prior to his murder. What did he want?")
            print("4 - No further questions.")
            print()

            try:
                selection = int(input("What would you like to ask Mr. George? "))
                print()

                if (selection == 4):
                    print("Right, back to the others.")
                    done = True
                    break

                if (isGuilty == True):
                    print(self.murdererResponses[selection - 1])
                    print()
                    time.sleep(1)
                else:
                    print(self.innocentResponses[selection - 1])
                    print()
                    time.sleep(1)

                done = False

                continue 

            except:
                print("Sorry, we could not understand you.\n")
                continue 

        return

class _Smallweed:
    name = "Grandfather Smallweed"
    greeting = "Bah get off my lawn. How could I have possibly killed anyone"

    murdererResponses = ["I was off doing cartwheels in the snow. Where do you think I was?", "He was my lawyer. He wasn't a good one either.", "I'm glad he got was coming to him."]
    innocentResponses = ["I was off doing cartwheels in the snow. I was here in my chair, like I always have been.", "He's my lawyer, and a pretty pathetic one at that.", "He's a no good liar of a lawyer and I'm glad he got what was coming to him."]

    accused = "\"I'll smash you. I'll crumble you. I'll powder you. Go to the devil!\" - Grandfather Smallweed *Throws his pipe at you*"

    def introduction(self):
        print("####################################")
        print("#       Grandfather Smallweed      #")
        print("####################################")
        print(self.greeting)
        print()
        time.sleep(1)

    def question(self, isGuilty):
        self.introduction()

        done = False
        while not done:
            print("1 - Where were you the night Mr. Tulkinghorn was murdered?")
            print("2 - What was your relationship with Mr. Tulkinghorn like, prior to his murder?")
            print("3 - Mr. George was able to weasle his way out of paying you with Tulkinghorn's help. What do you think about that?")
            print("4 - No further questions.")
            print()

            try:
                selection = int(input("What would you like to ask Grandfather Smallweed? "))
                print()

                if (selection == 4):
                    print("Right, back to the others.")
                    time.sleep(.5)
                    print()
                    print("You'd better run you coward! - Grandfather Smallweed")
                    time.sleep(1)
                    done = True
                    break

                if (isGuilty == True):
                    print(self.murdererResponses[selection - 1])
                    print()
                    time.sleep(1)
                else:
                    print(self.innocentResponses[selection - 1])
                    print()
                    time.sleep(1)

                done = False

                continue 

            except:
                print("Sorry, we could not understand you.\n")
                continue 

        return

class _Hortense:
    name = "Mademoiselle Hortense"
    greeting = "Tulkinghorn had many enemies, not in the least of which was the tretcherous Lady Dedlock, why not ask her about the matter?"

    murdererResponses = ["I have nothing to say to you or your cursed wife.", "He had some information I wanted to buy from him.", "Ha. As if I cared enough about her to do anything like that."]
    innocentResponses = ["I was trying to pick up the pieces of my life, thanks.", "He was my mistress's husband's lawyer. Did you want to know about his dog too?", "No. I hate her, but she will fall on her own."]

    accused = "\"Where is your false, your tretcherous, and cursed wife? I would love to tear her, limb from limb.\" - Mademoiselle Hortense"

    def introduction(self):
        print("####################################")
        print("#       Mademoiselle Hortense      #")
        print("####################################")
        print(self.greeting)
        print()
        time.sleep(1)

    def question(self, isGuilty):
        self.introduction()

        done = False
        while not done:
            print("1 - Where were you the night Mr. Tulkinghorn was murdered?")
            print("2 - What was your relationship with Mr. Tulkinghorn like, prior to his murder?")
            print("3 - You had some issues with Lady Dedlock, if I recall. Could you have murdered Mr. Tulkinghorn to frame it on Lady Dedlock?")
            print("4 - No further questions.")
            print()

            try:
                selection = int(input("What would you like to ask Mademoiselle Hortense?"))
                print()

                if (selection == 4):
                    print("Right, back to the others.")
                    done = True
                    break

                if (isGuilty == True):
                    print(self.murdererResponses[selection - 1])
                    print()
                    time.sleep(1)
                else:
                    print(self.innocentResponses[selection - 1])
                    print()
                    time.sleep(1)

                done = False

                continue 

            except:
                print("Sorry, we could not understand you.\n")
                continue 

        return

class _Esther:
    name = "Esther"
    greeting = "I'm so sorry, but I didn't do it! I could never harm anyone!"

    murdererResponses = ["I was home, in Bleak House", "He is involved in the Jarndyce & Jarndyce case, I think. \nAside from that, I'm not sure I had much of a relationship with him.", "Nothing at all! Why would I murder Mr. Tulkinghorn??"]
    innocentResponses = ["I was home, in Bleak House", "He is involved in the Jarndyce & Jarndyce case, I think. \nAside from that, I'm not sure I had much of a relationship with him.", "Nothing at all! Why would I murder Mr. Tulkinghorn??"]

    accused = "\"I went, I was passing quickly on, and in a few moments should have passed the lighted window, \nwhen my echoing footsteps brought it suddenly into my mind that there was a dreadful \ntruth in the legend of the Ghost's Walk; that it was I, who was to bring \ncalamity upon the stately house; and that my warning feet were haunting it even then.\" - Esther Summerson"

    def introduction(self):
        print("####################################")
        print("#         Esther Summerson         #")
        print("####################################")
        print(self.greeting)
        print()
        time.sleep(1)

    def question(self, isGuilty):
        self.introduction()

        done = False
        while not done:
            print("1 - Where were you the night Mr. Tulkinghorn was murdered?")
            print("2 - What was your relationship with Mr. Tulkinghorn like, prior to his murder?")
            print("3 - What could you have possibly gained from murdering Tulkinghorn?")
            print("4 - No further questions.")
            print()

            try:
                selection = int(input("What would you like to ask Esther?"))
                print()

                if (selection == 4):
                    print("Right, back to the others.")
                    done = True
                    break

                if (isGuilty == True):
                    print(self.murdererResponses[selection - 1])
                    print()
                    time.sleep(1)
                else:
                    print(self.innocentResponses[selection - 1])
                    print()
                    time.sleep(1)

                done = False

                continue 

            except:
                print("Sorry, we could not understand you.\n")
                continue 

        return
