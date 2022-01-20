import random
from data import data
from art import logo, vs
from replit import clear

def get_account():
  return random.choice(data)

def format_data(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"

def answer(guess, a, b):
  if a > b:
    return guess == "a"
  else:
    return guess == "b"


def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = get_account()
  account_b = get_account()

  while game_should_continue:
    account_a = account_b
    account_b = get_account()

    while account_a == account_b:
      account_b = get_account()

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_count = account_a["follower_count"]
    b_count = account_b["follower_count"]
    is_correct = answer(guess, a_count, b_count)

    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()
