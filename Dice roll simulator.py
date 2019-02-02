import random
import time

numbers = ["1","2","3","4","5","6"]

def question():
   question = input("Input any key to roll the dice")

def roll():
   time.sleep(0.7)
   print("")
   print("Rolling . . .")
   time.sleep(0.7)
   print("")
   print("Rolling . . .")
   time.sleep(0.7)
   print("")
   print("Rolling . . .")
   time.sleep(0.7)
   print("")
   random_choice = random.choice(numbers)
   print("Your number is:",random_choice)

def again():
   yes = ["Y", "y"]
   print("")
   question_yes_no = input("Do you want to roll again? [Y or N] ")
   print(" ")
   if question_yes_no in yes:
      question()
      roll()
      again()
   else:
      print("Bye!")
      exit()

question()
roll()
again()
