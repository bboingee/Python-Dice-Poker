from random import randint
import string


def roll():  # Rolling dice for a number
    dice = ['1', '2', '3', '4', '5', '6']
    pick = dice[randint(0, 5)]
    return pick


def pick():  # The hand of roll
    i = 0
    hand = []
    while i <= 4:
        hand.insert(i, roll())
        i += 1
    else:
        return hand


def cardset(y):
    temp = y
    pair = ([x for x in temp if temp.count(x) > 1 and y.count(x) < 3])
    triple = ([x for x in temp if temp.count(x) == 3])
    four = ([x for x in temp if temp.count(x) == 4])
    str1 = [1, 2, 3, 4, 5]
    str2 = [2, 3, 4, 5, 6]
    if len(pair) == 2:
        print("You have one pair of ", pair[0], ".")
    elif len(pair) == 4:
        pair.sort()
        print("You have two pair of ", pair[0], " and", pair[2], ".")
    elif len(triple) == 3 and len(pair) == 2:
        triple.sort()
        print("You have Full House.", "Three of", triple[0], "and one pair of ", pair[0], ".")
    elif len(triple) == 3 and len(pair) != 2:
        print("You have three kind of", triple[0], ".")
    elif len(four) == 4:
        print("You have four kind of", four[0], ".")
    elif y == str1 or y == str2:
        print("You have a straight", y)
    else:
        print("You have no hand")


def again(z):
    print(z)
    i = 0
    while i <= 4:
        try:
            n = i + 1
            print ("Dice Number # : ", n)
            change = str(input("Would you like to reroll the dice? Type Y or N : "))
            if change == "Y" or change == "y":
                z[i]=roll()
                i += 1
            elif change == "N" or change == "n":
                i += 1

            elif change != "Y" or change != "y":
                raise IOError
        except IOError:
            print ("You did not enter Y or N.")
    return z


def main():
    player = []
    player = pick()
    print("You have rolled ", player)
    cardset(player)
    again(player)
    print("Your final dices are", player)
    cardset(player)



# Only main after this line

main()
