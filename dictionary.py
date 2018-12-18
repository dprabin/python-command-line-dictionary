'''
This contains all the code required to read word meanings from data file to match the user input.
'''
import json
from difflib import get_close_matches

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
            return "The word doesn't exist in our dictionary"
        else:
            return "You should have entered either y or n."
    else:
        return "The word doesn't exist."

word = input("Enter the Word: ")
output = meaning(word)
for item in output:
    print (item)
