# Python program for a dictionary
# Known issue: data is loaded from a json each session
#              which is very expensive if the json file
#              becomes bigger


# The website for info on the Python Standard Library
# https://docs.python.org/3/library/

import json
from difflib import get_close_matches
# To find the close matches if the user made a typo

# storing the contents of the dictionary in the json file as a python dictionary
data = json.load(open("data.json"))
# print("Type of data:",type(data))

def translate(word):
    
    word = word.lower()
    
    if word in data:
        return data[word]
    
    elif word.title() in data: # if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]

    elif word.upper() in data: # to handle acronyms like USA or NATO
        return data[word.upper()]
    
    elif len(get_close_matches(word, data.keys())) > 0:
        option = input("Did you mean %s instead ?\nEnter Y if yes, or N for no: " % get_close_matches(word, data.keys())[0]).upper() # to handle y, Y, n, N
        if option == "Y":
            return data[get_close_matches(word, data.keys())[0]]
            # The first item is the best match thus, [0] is used
        elif option == "N":
            return "The word doesn't exist. Please double check it !"

        else:
            return "I didn't understand your option entry."

    else:
        return "The word doesn't exist. Please double check it !"

word = input("Enter word: ")

output = translate(word)

# The answer from the function can be either:
    # list: if there is a definition
    # str: if a message is sent to the user from the program indicating a special case
if type(output) == list:
    # to display the different definitions in a numbered format
    for definition in enumerate(output):
        print(definition[0]+1,":",definition[1])
else:
    print(output)