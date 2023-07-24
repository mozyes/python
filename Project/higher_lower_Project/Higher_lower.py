import random
from art import logo, vs
from game_data import data
from replit import clear

def game(player_score):
  print(logo)
  if player_score > 0:
    print("You are correct!")
  compare_first = random.choice(data)
  print(f' Compare A: {compare_first["name"]}, {compare_first["description"]}, from {compare_first["country"]}')
  print(vs)
  compare_second = random.choice(data)
  print(f' Compare B: {compare_second["name"]}, {compare_second["description"]}, from {compare_second["country"]}')
  player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
  if compare_first["follower_count"] > compare_second["follower_count"] and player_choice == 'a':
    player_score += 1
  elif compare_first["follower_count"] < compare_second["follower_count"] and player_choice == 'b':
    player_score += 1
  else:
    clear()
    print(f"Oops! You are incorrect. Your total score is {player_score}")
    if input("Do you want to replay again? Type 'y' or 'n': ").lower() == 'n':
      return player_score, False  # Return False when player chooses not to replay
  return player_score, True

player_score = 0
replay = True
while replay:
    clear()
    player_score, replay = game(player_score)
