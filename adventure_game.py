import time
import sys
import random
places = ['house', 'cave', 'house2']
monsters = ['pirate', 'troll', 'wicked fairie', 'dragon', 'gorgon']
result = ['yes', 'no']
user_option = ['1', '2']
list = []
random_item = random.choice(monsters)


def print_pause(message):
    print(message)
    time.sleep(2)


def intro():
    print_pause("You find yourself in a dark dungeon.")
    print_pause("In front of you are two passageways.")
    print_pause("Which way do you want to go?")


def choice():
    user_choice = ""
    print("\nEnter 1 to knock on the door of the house.\n")
    print("Enter 2 to peer into the cave.")
    while user_choice not in user_option:
        user_choice = input("(Please enter 1 or 2.)\n")

    if user_choice == user_option[0]:
            house()

    elif user_choice == user_option[1]:
            cave()


def play_agin():
    play = input("Would you like to play again? (yes/no)\n")
    if play == result[0]:
        print_pause("Excellent! Restarting the game ...\n\n")
        intro()
        choice()
    elif play == result[1]:
        print_pause("Thanks for playing! See you next time.")
        sys.exit()
    else:
        play_agin()


def house():
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door"
                "opens and out steps a "+random_item)
    print_pause("Eep! This is the " + random_item + " house!")
    print_pause("The " + random_item + " attacks you!")
    if "sword" in list:
        house2()
    else:
        print_pause("You feel a bit under-prepared for this,"
                    "what with only having a tiny dagger.\n")
        invalid()


def invalid():
    fight_or_run = input("Would you like to (yes) fight or (no) run away?\n")
    if fight_or_run == result[0]:
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the "+random_item)
        print_pause("You have been defeated!")
        play_agin()
    elif fight_or_run == result[1]:
        print_pause("You run back into the field. Luckily,"
                    "you don't seem to have been followed.")
        choice()
    else:
        while fight_or_run != result[0] or fight_or_run != result[1]:
            play_agin()


def cave():
    print_pause("You peer cautiously into the cave.")
    if "sword" not in list:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and"
                    "take the sword with you.")
        print_pause("You walk back out to the field.")
        list.append("sword")
        choice()
    else:
        print_pause("You've been here before, and gotten all the good stuff."
                    "It's just an empty cave now.")
        print_pause("You walk back out to the field.")
        choice()


def house2():
    fight_or_run = input("Would you like to (1) fight or (2) run away?\n")
    if fight_or_run == result[0]:
        print_pause("As the dragon moves to attack,"
                    " you unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand"
                    "as you brace yourself for the attack.")
        print_pause("But the dragon takes one look at your"
                    " shiny new toy and runs away!")
        print_pause("You have rid the town of the dragon. You are victorious!")
        play_agin()
    elif fight_or_run == result[1]:
        print_pause("You run back into the field. Luckily,"
                    "you don't seem to have been followed.")
        choice()
    else:
        while fight_or_run != result[0] or fight_or_run != result[1]:
            play_agin
intro()
choice()
invalid()
cave()
house2()

