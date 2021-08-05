#!/usr/bin/env python3
import requests
import random
# Define our "base" API
API = "https://opentdb.com/api.php?amount=10&category=15&difficulty=easy&type=multiple"
def main():
    """Run time code"""
    user_score = 0

    resp = requests.get(API)
    questions  = resp.json()


    for data in questions["results"]:
      multiple_choice = data["incorrect_answers"]
      multiple_choice.append(data["correct_answer"])
      random.shuffle(multiple_choice)

      # Displays Questions
      print(data["question"])

      choices = {"a": multiple_choice[0], "b": multiple_choice[1], "c": multiple_choice[2], "d": multiple_choice[3]}

      for answer in choices.keys():
        print(answer.upper() + ".) " + choices[answer])
      while True: 
          ans = input("> ").lower()

          if ans in choices.keys():
            break
          else:
            print("Invalid input")
            print(data["question"])
            for answer in choices.keys():
              print(answer.upper() + ".) " + choices[answer])
      if choices[ans] == data["correct_answer"]:
        print("Correct!!")
        user_score += 1
      else:
        print("Wrong, the correct answer is: " + data["correct_answer"])

    
    print('You got ' + str(user_score) + " correct out of " + str(len(questions["results"])) + " correct")

if __name__ == "__main__":
    main()
