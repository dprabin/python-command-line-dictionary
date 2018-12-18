'''
This contains all the code required to read word meanings from data file to match the user input.
'''
import json
from difflib import get_close_matches
get_close_matches("pototo") #use sequenceMatcher to ets most similar word out of the keys in dictionary

data = json.load(open("data.json"))

def meaning(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input("Did you mean %s instead? Yes or No? " % get_close_matches(w,data.keys())[0])
        if yn == 'y':
            return data[get_close_matches(w,data.keys())[0]]
        elif yn =='n':
            return "You should have entered either y or n"
        else:
            return "The word doesnt exist."
    else:
        return "The word doesn't exist."

word = input("Enter the Word: ")
print(meaning(word))
