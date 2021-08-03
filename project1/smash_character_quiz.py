light = ["Kirby", "Yoshi", "Pikachu", "Jigglypuff", "Ness"]
medium = ["Mario", "Luigi", "Samus", "Fox"]
heavy = ["Captain Falcon", "Donkey Kong", "Link"]
choices_input = ['1', '2', '3']

user_score = 0

def main():
    game = True
    while game: 
      question_1 = input(
        '''When you play a match, which do you prefer?

        1. I like to tire them out and run the clock
        2. Hit hard and win fast
        3. Watch my oponent and see how they move
 
 > '''
      )
      if question_1 in choices_input:
        print("success")
      else:
        print("fail")
        game = False

      question_2 = input(
        '''How do you deal with Projectiles?

        1. Meh
        2. I love using them
        3. Doesn't bother me
 
 > '''
      )
      if question_2 in choices_input:
        print("success")
      else:
        print("fail")
        game = False

if __name__ == "__main__":
  main()
