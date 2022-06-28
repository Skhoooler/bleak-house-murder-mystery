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

            match person:
                case 1:
                    return engine.dedlock.question
                case 2:
                    return engine.george.question
                case 3:
                    return engine.smallweed.question
                case 4:
                    return engine.hortense.question
                case 5:
                    return engine.esther.question
                case 6:
                    questioning = False
                    return 
        
        except ValueError:
            print()
            print("Please tell me who you would like to talk to (type in 1-6)")

    

if __name__ == "__main__":
    main()