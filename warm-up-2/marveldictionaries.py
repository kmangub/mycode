#!/usr/bin/env python3

marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"She-Hulk":
  {"real name": "jennifer walters",
  "powers": "super strength & intelligence",
  "archenemy": "Titania"}
             }
play_again = True

while play_again:
    char_name = input("Which character do you want to know about? (Starlord, Mystique, or She-Hulk \n").lower()
    char_stat = input("What statistic do you want to know about? (real name, powers, archenemy \n").lower()

    print(f"{char_name.title()}'s {char_stat.title()} is: {marvelchars[char_name.title()][char_stat]}\n")

    ask = input("Would you like to play again? (y or n) \n ")

    if ask == "n":
        play_again = False


