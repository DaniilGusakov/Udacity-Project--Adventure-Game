import time
import random
import sys


def print_pause(string):
    print(string)
    time.sleep(2)


def game_over():
    gm = input("1 To play again/ 2 To stop playing\n")
    if gm == '1':
        play_game()
    elif gm == '2':
        sys.exit()
    else:
        print_pause("Try again")
        game_over()


def intro(enemy, weapon, cave2r):
    print_pause("You woke up in a deep, dark cave.")
    print_pause("You are slowly standing up, and look around.")
    print_pause("You notice a rock laying nearby.")
    rock = input("1 You pick up the rock/ 2 You leave the rock behind \n")
    while rock != '1' or rock != '2':
        if rock == '1':
            print_pause("You picked up a pretty small rock")
            weapon = 'rock'
            cave1(enemy, weapon, cave2r)
        elif rock == '2':
            print_pause("You left the rock behind, "
                        "and are looking for a way out")
            cave1(enemy, weapon, cave2r)
        else:
            print_pause("Try again.")
            rock = input("1 You pick up the rock/"
                         "2 You leave the rock behind \n")


def cave2_left(enemy, weapon, cave2r):
    print_pause("This cave seems to be pretty small.")
    print_pause("You carefully walk through the dark cave.")
    print_pause("At the end you see a massive sword stuck between two rocks.")
    cave_left = input("1 You try to take the sword/ 2 You go back \n")
    while cave_left != '1' or cave_left != '2':
        if cave_left == '1':
            print_pause("You try to grab the sword,"
                        "but it is stuck very hard.")
            print_pause("You can also feel how the "
                        "ground is shaking a little.")
            massword = input("1 Try harder/ 2 Run back \n")
            while massword != '1' or massword != '2':
                if massword == '1':
                    print_pause("Using all the strength you have,"
                                " you are able to get the sword.")
                    print_pause("Everything around you is starting "
                                "to shake very hard.")
                    print_pause("Rocks start to "
                                "fall from above.")
                    print_pause("When you open your eyes again,"
                                " you see only darkness.")
                    print_pause("You are trying to find the way out.")
                    print_pause("The fallen rocks are blocking the way back")
                    print_pause("You try to move them,"
                                " but you are not strong enought")
                    print_pause("You are stuck in this cave now")
                    print_pause("GAME OVER")
                    game_over()
                    break
                elif massword == '2':
                    print_pause("You leave the sword behind, and run away.")
                    print_pause("You come back to where you started")
                    cave1(enemy, weapon, cave2r)
                else:
                    print_pause("Try again")
                    massword = input("1 Try harder/ 2 Run back \n")
                break
        elif cave_left == '2':
            print_pause("You decide to turn back.")
            print_pause("You come back to where you started")
            cave1(enemy, weapon, cave2r)
        else:
            print_pause("Try again")
            cave_left = input("1 You try to take the sword/ 2 You go back \n")


def cave2_right(enemy, weapon, cave2r):
    print_pause("After walking through a dark cave for a few minutes,")
    print_pause("you see a long and wide corridor with"
                " a lot of ancient paintings on the walls.")
    print_pause("You walk through the corridor amazed by what you see there")
    if cave2r == 1:
        print_pause("You accidently notice a dice on the floor")
        print_pause("The dice is shining, it is probably magical")
        cave2r = 0
        fun = input("1 Roll a dice/ 2 Continue walking straight \n")
        while fun != '1' or fun != '2':
            if fun == '1':
                dice = random.randint(1, 6)
                print_pause("The dice stopped at number " + str(dice))
                if dice == 1:
                    print_pause("The Dwarf Steel Sword appeared in front of you")
                    sword = input("1 Take the sword(You will lose the "
                                  "rock if you had it)/ 2 Leave the sword \n")
                    while True:
                        if sword == '1':
                            print_pause("You picked up the sword")
                            weapon = 'sword'
                            cave3(enemy, weapon, cave2r)
                        elif sword == '2':
                            print_pause("You left the sword on the ground")
                            cave3(enemy, weapon, cave2r)
                        else:
                            print_pause("Try again")
                            sword = input("1 Take the sword(You will lose the rock"
                                          " if you had it)/ 2 Leave the sword \n")
                elif dice == 2:
                    print_pause("The Elven Bow appeared in front of you")
                    bow = input("1 Take the bow(You will lose the rock if"
                                "you had it)/ 2 Leave the bow \n")
                    while True:
                        if bow == '1':
                            print_pause("You picked up the bow")
                            weapon = 'bow'
                            cave3(enemy, weapon, cave2r)
                        elif bow == '2':
                            print_pause("You left the bow on the ground")
                            cave3(enemy, weapon, cave2r)
                        else:
                            print_pause("Try again")
                            bow = input("1 Take the bow(You will lose the rock "
                                        "if you had it)/ 2 Leave the bow \n")
                elif dice == 3:
                    print_pause("The Old Magic Staff appeared in front of you")
                    staff = input("1 Take the staff(You will lose the rock if "
                                  "you had it)/ 2 Leave the staff \n")
                    while True:
                        if staff == '1':
                            print_pause("You picked up the staff")
                            weapon = 'staff'
                            cave3(enemy, weapon, cave2r)
                        elif staff == '2':
                            print_pause("You left the staff on the ground")
                            cave3(enemy, weapon, cave2r)
                        else:
                            print_pause("Try again")
                            staff = input("1 Take the staff(You will lose the rock"
                                          " if you had it)/ 2 Leave the staff \n")
                elif dice == 4:
                    print_pause("The floor under you desapeared and "
                                "you fell into the void")
                    print_pause("GAME OVER")
                    game_over()
                    break
                elif dice == 5:
                    print_pause("The magic waves began to whirl around you.")
                    print_pause("In a few second everything went dark.")
                    print_pause("You returned back to the starting cave")
                    cave1(enemy, weapon, cave2r)
                elif dice == 6:
                    print_pause("The dice just desapeared")
                    print_pause("You have no other choice except "
                                "just going straight")
                    cave3(enemy, weapon, cave2r)
            elif fun == '2':
                print_pause("You went by the dice and continued"
                            " you walk through the corridor.")
                cave3(enemy, weapon, cave2r)
            else:
                print_pause("Try again")
                fun = input("1 Roll a dice/ 2 Continue walking straight")
    else:
        print("This "
              "time you don't see the dice on the floor.")
        cave3(enemy, weapon, cave2r)

def cave3(enemy, weapon, cave2r):
    print_pause("At the end of the corridor you find a massive door.")
    print_pause("You push it and see a " + enemy + " standing in "
                "the middle of a giant circular room")
    print_pause("Behind a " + enemy + " you see an old wooden door")
    print_pause("Small beams of sunlight are going under it")
    print_pause("You realize that this is the only way out of this place")
    print_pause("But to get to the door, you need "
                "to defeat a " + enemy + " first")
    cave3 = input("1 Fight/ 2 Run away \n")
    while cave3 != '1' or cave3 != '2':
        if cave3 == '1':
            if enemy == 'dragon':
                if weapon == 'rock':
                    print_pause("One very accurate throw of your rock "
                                "was able to break the dragon's skull.")
                    print_pause("You defeated the dragon")
                    print_pause("The path is clear now!")
                    print_pause("You open the old wooden door and "
                                "get to a big green field")
                    print_pause("You escaped the dungeon!")
                    print_pause("Congritulations! You won!")
                    game_over()
                elif weapon == 'nothing':
                    print_pause("You will have to fight the"
                                " dragon with your bare hands")
                    print_pause("Turns out the dragon is better at fist fight")
                    print_pause("GAME OVER")
                    game_over()
                else:
                    print_pause("You took your " + weapon)
                    print_pause("But the dragon melted you "
                                "with his fire breath")
                    print_pause("GAME OVER")
                    game_over()
            elif enemy == 'witch':
                if weapon == 'rock':
                    print_pause("One very good throw of your rock was "
                                "able to leave the witch unconscious.")
                    print_pause("You defeated the witch.")
                    print_pause("The path is clear now!")
                    print_pause("You open the old wooden door and"
                                " get to a big green field")
                    print_pause("You escaped the dungeon!")
                    print_pause("Congritulations! You won!")
                    game_over()
                elif weapon == 'nothing':
                    print_pause("You were ready to fight the "
                                "witch with you bare hand,")
                    print_pause("but got turned into a frog")
                    print_pause("GAME OVER")
                    game_over()
                else:
                    print_pause("You prepared to fight the witch "
                                "with your " + weapon + ",")
                    print_pause("But she rapidly turned you into a frog")
                    print_pause("GAME OVER")
                    game_over()
            else:
                if weapon == 'rock':
                    print_pause("By lifting your rock,"
                                " you scared the dog away")
                    print_pause("The path is clear now!")
                    print_pause("You open the old wooden door and "
                                "get to a big green field")
                    print_pause("You escaped the dungeon!")
                    print_pause("Congritulations! You won!")
                    game_over()
                else:
                    print_pause("Before you even prepared to fight, the "
                                "dog bit you so hard ,that you lost")
                    print_pause("GAME OVER")
                    game_over()

        elif cave3 == '2':
            print_pause("You run back to where you started")
            cave1(enemy, weapon, cave2r)
        else:
            print_pause("Try again")
            cave3 = input("1 Fight/ 2 Run away")


def cave1(enemy, weapon, cave2r):
    print_pause("You see two paths in front of you.")
    print_pause("You can either go left or right.")
    path = input("1 to chose the left path/ 2 to chose the right path. \n")
    while path != 'left' or path != 'right':
        if path == '1':
            print_pause("You enter the cave on the left")
            cave2_left(enemy, weapon, cave2r)
        elif path == '2':
            print_pause("You enter the cave on the right")
            cave2_right(enemy, weapon, cave2r)
        else:
            print_pause("Try again")
            path = input("1 to chose the left path/"
                         "2 to chose the right path \n")


def play_game():
    cave2r = 1
    weapon = 'nothing'
    enemy = random.choice(['dragon', 'witch', ' small dog'])
    intro(enemy, weapon, cave2r)


play_game()
