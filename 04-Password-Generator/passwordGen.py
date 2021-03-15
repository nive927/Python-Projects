"""
Password Generator
"""
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
n_letters= int(input("How many letters would you like in your password?\n")) 
n_symbols = int(input(f"How many symbols would you like?\n"))
n_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

for character in range(0, n_letters):
  password += random.choice(letters)

for character in range(0, n_symbols):
  password += random.choice(symbols)

for character in range(0, n_numbers):
  password += random.choice(numbers)

print(f"Your password is {''.join(random.sample(password,len(password)))}")
# SHUFFLE causes error as it is INPLACE but SAMPLE returns a new list
# print(f"Your password is {random.shuffle(password)}")
# To use shuffle do it like this
"""
random.shuffle(list(password))#NOTE: Shuffle is inplace, doesn't return anything. That is why ''.join(random.shuffle(list(password))) won't work as join gets None.

print(f"Your password is {''.join(password)}")
"""

"""
SAMPLE
Syntax : random.sample(sequence, k)

Parameters:
sequence: Can be a list, tuple, string, or set.
k: An Integer value, it specify the length of a sample.

Returns: k length new list of elements chosen from the sequence.

SHUFFLE
Syntax : random.shuffle(sequence, function)

Parameters:
sequence: Can be a list, tuple, string, or set.
function: Optional. The name of a function that returns a number between 0.0 and 1.0.
If not specified, the function random() will be used
"""



