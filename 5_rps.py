import sys
import random
from enum import Enum

game_count = 0

def play_rps():

  class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    
  #User input

  # value = input('Please enter a value: \n')
  # print(value)

  player_choice = input("\nEnter ... \n1 for Rock \n2 for Paper, or \n3 for Scissors: \n\n")

  if player_choice not in ["1", "2", "3"]:
    print('"You must enter 1, 2, or 3."')
    return play_rps()
  
  player = int(player_choice)
    
  computer_choice = random.choice("123")

  computer = int(computer_choice)

  print("\nYou chose " + str(RPS(player)).replace('RPS.', '') + "." )
  print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".\n" )
  def decide_winner(player, computer):
    if player == 1 and computer == 3 :
      return "🏆 player wins"
    elif player == 2 and computer == 1:
      return "🏆 player wins"
    elif player == 3 and computer == 2:
      return "🏆 player wins"
    elif player == computer:
      return "😳 tie game!"
    else:
      return "🐍 Python wins"
    
  game_result = decide_winner(player, computer)
  
  print(game_result)
    
  global game_count
  game_count += 1 
  
  print("\n Game count:" + " " + str(game_count))
  print("\nPlay again?")
  
  while True: 
    play_again = input("\nY for Yes or \nQ to Quit \n")
    if play_again.lower() not in ["y", "q"]: 
      continue
    else: 
      break
   
  if play_again.lower() == "y": 
    return play_rps()
  else: 
    print("\n🎉🎉🎉🎉")
    print("Thank you for playing\n")
    sys.exit("Bye! 👋")
    #you can also use break()
    
play_rps()
  
