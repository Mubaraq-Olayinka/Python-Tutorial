import sys
import random
from enum import Enum

def rps(name='PlayerOne'):
  game_count = 0
  player_wins = 0
  python_wins = 0

  def play_rps():
    nonlocal name
    nonlocal player_wins
    nonlocal python_wins
    
    class RPS(Enum):
      ROCK = 1
      PAPER = 2
      SCISSORS = 3
      
    #User input

    # value = input('Please enter a value: \n')
    # print(value)

    player_choice = input(f"\n{name}, please enter ... \n1 for Rock \n2 for Paper, or \n3 for Scissors: \n\n")

    if player_choice not in ["1", "2", "3"]:
      print(f"{name}, please enter 1, 2, or 3.")
      return play_rps()
    
    player = int(player_choice)
      
    computer_choice = random.choice("123")

    computer = int(computer_choice)

    print(f"\n{name}, you chose {str(RPS(player)).replace('RPS.', '')}." )
    print(f"Python chose {str(RPS(computer)).replace('RPS.', '')}.\n" )
    def decide_winner(player, computer):
      nonlocal name
      nonlocal player_wins
      nonlocal python_wins
      if player == 1 and computer == 3 :
        player_wins += 1
        return f"🏆 {name} wins"
      elif player == 2 and computer == 1:
        player_wins += 1
        return f"🏆 {name} wins"
      elif player == 3 and computer == 2:
        player_wins += 1
        return f"🏆 {name} wins"
      elif player == computer:
        return "😳 tie game!"
      else:
        python_wins += 1
        return f"🐍 Python wins!\n Sorry {name}.. 😢"
      
    game_result = decide_winner(player, computer)
    
    print(game_result)
      
    nonlocal game_count
    game_count += 1 
    
    print(f"\n Game count: {game_count}")
    print(f"\n {name}'s wins: {player_wins}")
    print(f"\n Python wins: {python_wins}")
    
    print(f"\nPlay again, {name}?")
    
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
      print("Thank you for playing!\n")
      sys.exit(f"Bye {name}!! 👋")
      #you can also use break()
  return play_rps    

if __name__ == "__main__" :
  import argparse

  parser = argparse.ArgumentParser(
    description="Provides an personalized experience."
  )

  parser.add_argument(
    "-n", "--name", metavar="name", required=True, help="The name of the person playing the game."
  )

  args = parser.parse_args()
  rock_paper_scissors = rps(args.name)
  rock_paper_scissors()
  
