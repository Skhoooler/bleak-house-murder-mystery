################################################
# Bleak House Murder Mystery
# 
# A small murder mystery game with python
################################################
import suspects
import time

def main():
    engine = suspects.Suspects()

    print("hello world")
    print("###############################################")
    print("#         Bleak House Murder Mystery          #")
    print("#              by David Doria                 #")
    print("###############################################")
    print("")
    print("Inspector Bucket! I'm so glad you are here!\nMr. Tulkinghorn has been murdered and")
    print("It's up to you to figure out who has committed this")
    print("heinous crime! Here are our suspects: ")
    print()
    time.sleep(6) # For dramatic effect
    print("Lady Dedlock")

    time.sleep(2)
    print("Mr. George")

    time.sleep(2)
    print("Grandfather Smallweed")
    
    time.sleep(2)
    print("Mademoiselle Hortense")
    
    time.sleep(2)
    print("and last, but not least,")

    time.sleep(4)
    print("Esther Summerson")
    time.sleep(1.5)

    print()
    print("Here is what we know...")
    time.sleep(1)

    print()
    print("He was murdered " + engine.weapon + " on the 21st night of January, 1850.")
    time.sleep(2)

    print()
    for clue in engine.clues:
        print(clue)
        time.sleep(2)

    time.sleep(1)
    print()
    print("We brought all of the suspects for you to question.")

    
    time.sleep(1)
    questioning = True

    while (questioning):
        print()
        print("1 - Lady Dedlock")
        print("2 - Mr. George")
        print("3 - Grandfather Smallweed")
        print("4 - Mademoiselle Hortense")
        print("5 - Esther Summerson")
        print("6 - I am done questioning")

        try:
            print()
            person = int(input("Who would you like to speak to? "))
            print()

            match person:
                case 1:
                    if (engine.murderer == engine.dedlock):
                        engine.dedlock.question(True)
                    else:
                        engine.dedlock.question(False)
                case 2:
                    if (engine.murderer == engine.george):
                        engine.george.question(True)
                    else:
                        engine.george.question(False)
                case 3:
                    if (engine.murderer == engine.smallweed):
                        engine.smallweed.question(True)
                    else:
                        engine.smallweed.question(False)
                case 4:
                    if (engine.murderer == engine.hortense):
                        engine.hortense.question(True)
                    else:
                        engine.hortense.question(False)
                case 5:
                    if (engine.murderer == engine.esther):
                        engine.esther.question(True)
                    else:
                        engine.esther.question(False)
                case 6:
                    confirm = input("Alright Inspector Bucket, are you ready to name the murderer? (Y/N)")

                    if (confirm == "Y" or confirm == "y" or confirm == "N" or confirm == "n"):
                        if (confirm == "Y" or confirm == "y"):
                            questioning = False
                            break
                        else:
                            print("Ok. I'll bring the suspects back out.")
                            questioning = True
                    else:
                        print("Could you say that one more time Inspector Bucket? I couldn't understand you.")
                        questioning = True
        
        except ValueError:
            print()
            print("Please tell me who you would like to speak to. (type in 1-6)")
        
        #questioning = True
    
    print("Here are our suspects: ")
    print()
    print("1 - Lady Dedlock")
    print("2 - Mr. George")
    print("3 - Grandfather Smallweed")
    print("4 - Mademoiselle Hortense")
    print("5 - Esther Summerson")
    print()
    print("It is up to you to decide who the murderer is, Inspector Bucket.")

    murderer = 0
    deciding = True
    while deciding:
        try:
            murderer = int(input("Who murdered Mr. Tulkinghorn? "))
            print()
            if (murderer == 1):
                murderer = "Lady Dedlock"
                print(engine.dedlock.accused)
                time.sleep(2)
                print()
                break
            elif (murderer == 2):
                murderer = "Mr. George"
                print(engine.george.accused)
                time.sleep(2)
                print()
                break
            elif (murderer == 3):
                murderer = "Grandfather Smallweed"
                print(engine.smallweed.accused)
                time.sleep(2)
                print()
                break
            elif (murderer == 4):
                murderer = "Mademoiselle Hortense"
                print(engine.hortense.accused)
                time.sleep(2)
                print()
                break
            elif (murderer == 5):
                murderer = "Esther Summerson"
                print(engine.esther.accused)
                time.sleep(2)
                print()
                break
            else:
                print("We can't understand you. Please speak up.")
                continue

        except:
            print("Please speak up Inspector Bucket, we can't understand.")
            continue

    print("...")
    time.sleep(1)
    print("So you say " + murderer + " is the murderer?")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print()
    print(engine.murderer.name + " was the true murderer...")
    time.sleep(2)
    print("fin")

if __name__ == "__main__":
    main()