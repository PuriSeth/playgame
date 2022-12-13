import random

def get_random_number():
  return random.randint(1, 6)

def play_game():
  dice1 = get_random_number()
  dice2 = get_random_number()
  total = dice1 + dice2
  print(f'You rolled a {dice1} and a {dice2} for a total of {total}.')
  if total in [7, 11]:
    print('You win!')
  elif total in [2, 3, 12]:
    print('You lose!')
  else:
    point = total
    print(f'Your point is {point}.')
    while True:
      dice1 = get_random_number()
      dice2 = get_random_number()
      new_total = dice1 + dice2
      print(f'You rolled a {dice1} and a {dice2} for a total of {new_total}.')
      if new_total == point:
        print('You win!')
        break
      elif new_total == 7:
        print('You lose!')
        break

play_game()
