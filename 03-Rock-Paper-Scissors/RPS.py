"""
Program to simulate RPS - Rock, Paper and Scissors
"""

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

def num_to_hand_sign(num):

  switcher = {
    0: rock,
    1: paper,
    2: scissors}

  return switcher.get(num, "Invalid number! Enter only 0, 1 or 2.\n")

while True:
  player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
  print(num_to_hand_sign(player_choice))

  if player_choice in range(0, 3):
    break;

computer_choice = random.randint(0,2)

print(f"Computer chose:\n{num_to_hand_sign(computer_choice)}")

if player_choice == computer_choice:
  print("Draw")
else:
  if player_choice == 0:
    if computer_choice == 1:
      win = 'c'
    else:
      win = 'p'
  elif player_choice == 1:
    if computer_choice == 2:
      win = 'c'
    else:
      win = 'p'
  elif player_choice == 2:
    if computer_choice == 0:
      win = 'c'
    else:
      win = 'p'

if win == 'c':
  print("You lose")
else:
  print("You win")




