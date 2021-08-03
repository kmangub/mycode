#!/usr/bin/env python3

#Arrays
light = ["Kirby", "Yoshi", "Pikachu", "Jigglypuff", "Ness"]
medium = ["Mario", "Luigi", "Samus", "Fox"]
heavy = ["Captain Falcon", "Donkey Kong", "Link"]
choices_input = ['1', '2', '3']
questions = ['''When you play a match, which do you prefer?

        1. I like to tire them out and run the clock
        2. Watch my oponent and see how they move
        3. Hit hard and win fast
 
 >  ''', '''How do you deal with Projectiles?

        1. I love using them
        2. Meh
        3. Doesn't bother me
 
 >  ''', '''Both you and your opponent are at 300%. Tensions are high and friendships are on the line. What do you do?

        1. Down-B special FTW!
        2. Forward-Smash Attack and see them fly
        3. Throw your opponent to their demise
 
 >  ''']

def main():
    game = True
    user_score = 0

    print('''
      *****************************************************************
      **                                                             ** 
      **                  Super Smash Brothers 64                    **
      **                                                             **
      **                     Who Should I Choose                     **
      **                            Quiz                             **
      **                                                             ** 
      ***************************************************************** 
      ''')

    play = input("Type P to play or Q to quit: ").lower()
    while play:
        if play == 'p':
            game = True
            break
        if play == 'q':
            game = False
            break
        else:
            print("Incorrect input")
            play = input("Type P to play or Q to quit: ")

    while game:
        question_1 = input(questions[0])
        while question_1:
            if question_1 in choices_input:
                user_score += int(question_1)
                break
            else:
                print('Incorrect input. Please type 1, 2, or 3.')
                question_1 = input(questions[0])
        question_2 = input(questions[1])
        while question_2:
            if question_2 in choices_input:
                user_score += int(question_2)
                break
            else:
                print("Incorrect input")
                question_2 = input(questions[1])
        question_3 = input(questions[2])
        while question_3:
            if question_3 in choices_input:
                user_score += int(question_3)
                break
            else:
                print("Incorrect input")
                question_3 = input(questions[2])
        print("The characters for you would be: \n")
        if user_score < 5:
            for character in light:
                print(character)
            print(
                "\nAhh the floaty characters. With these guys, recovery is child's play. Now get back there and win!! \n"
            )
        if user_score >= 5 and user_score < 8:
            for character in medium:
                print(character)
            print(
                "\nYou like to be in control of the situation, so these characters can help you control the battefield! \n"
            )
        if user_score > 8:
            for character in heavy:
                print(character)
            print(
                "\nYou can hit hard with these folks! Just watch out because their recovery is kinda wonky. \n"
            )

        play_again = input(
                "Would you like to play again? Y to play again, N to quit: ").lower(
            )

        while play_again:
            if play_again == "y":
                user_score = 0
                print("Playing again \n")
                break
            elif play_again == "n":
                game = False
                break
            else:
                print("Invalid input")
                play_again = input(
                    "Would you like to play again? Y to play again, N to quit: "
                ).lower()

    # print('your score:', user_score)

    print('Thank you for playing!!')


if __name__ == "__main__":
    main()
