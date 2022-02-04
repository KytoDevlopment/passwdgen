from random import randint
from pystyle import Colors, Colorate
import sys
import time


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)


print(Colorate.Horizontal(Colors.yellow_to_red, """
                                       .___
___________    ______ ________  _  ____| _/
\____ \__  \  /  ___//  ___/\ \/ \/ / __ |
|  |_> > __ \_\___ \ \___ \  \     / /_/ |
|   __(____  /____  >____  >  \/\_/\____ |
|__|       \/     \/     \/             \/
"""))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

capitalletters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                  'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
specialcharacters = ["&", "!", "=", "-", "_"]

print_slow("\nCombien de caractères voulez vous dans votre mot de passe ?")
caracnumber = int(input())

print_slow("\nVoulez vous des lettres minuscules dans votre mot de passe ? (y/n)")
minbool = input()
if minbool == "y":
    minbool = True
elif minbool == "n":
    minbool = False

print_slow("\nVoulez vous des lettres majuscules dans votre mot de passe ? (y/n)")
majbool = input()
if majbool == "y":
    majbool = True
elif majbool == "n":
    majbool = False

print_slow("\nVoulez vous des nombres dans votre mot de passe ? (y/n)")
nbbool = input()
if nbbool == "y":
    nbbool = True
elif nbbool == "n":
    nbbool = False

passwdfinal = ""
for i in range(caracnumber):
    # Letters + Capital + Nbr
    if minbool is True and majbool is True and nbbool is True:
        random3 = letters + capitalletters + numbers
        passwdfinal = str(passwdfinal) + str(random3[randint(0, 60)])
    # Letters
    if minbool is True and majbool is False and nbbool is False:
        passwdfinal = str(passwdfinal) + str(letters[randint(0, 25)])
    # Letters + Capital
    if minbool is True and majbool is True and nbbool is False:
        randomlc = letters + capitalletters
        passwdfinal = str(passwdfinal) + str(randomlc[randint(0, 51)])
    # Capital
    if minbool is False and majbool is True and nbbool is False:
        passwdfinal = str(passwdfinal) + str(majbool[randint(0, 25)])
    # Letters + Nbr
    if minbool is True and majbool is False and nbbool is True:
        randomlnbr = letters + numbers
        passwdfinal = str(passwdfinal) + str(randomlnbr[randint(0, 34)])
    # Capital + numbers
    if minbool is True and majbool is True and nbbool is False:
        randomncap = numbers + capitalletters
        passwdfinal = str(passwdfinal) + str(randomncap[randint(0, 34)])
    if minbool is False and majbool is False and nbbool is False:
        print("T'as cru que t'allais me la faire à l'envers :) le programme va quitter dans 5 secondes")
        time.sleep(5)
        quit()


print_slow(f"Votre mot de passe est {passwdfinal}")
