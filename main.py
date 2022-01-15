from art import logo, vs
from game_data import data
import random
from replit import clear

def format_data(account):
  """Format the account data into printable format"""
  account_name = account['name']
  account_descr = account['description']
  account_country = account['country']
  return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers,b_followers):
  """Take the user guess and follower counts and returns if they got it right"""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

def play_game():
  score = 0 
  # Display art
  print(logo)
  game_should_continue = True
  account_b = random.choice(data)

  while game_should_continue:
    # Generate a random account from the game data
    # Making account at position B become the next account at position A
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
      account_b = random.choice(data)
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    # Ask user for a guess
    guess = input("Who has more followers? 'A' or 'B': ").lower()
    # Check if user is correct
    ## Get follower count of each account
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    ## Use if statament to check if user is correct
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong! Final score: {score}")
  # Give user feedback on their guess
  # Score keeping
  # Make the game repeatable
  # Clear the screen between round
  while input("Do you want to play another game? Type 'Y' or 'N': ").lower() == 'y':
    clear()
    play_game()

play_game()