'''
This contains all the code required to read word meanings from data file to match the user input.
'''
import json

data = json.load(open("data.json"))

def meaning(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        return "The word doesn't exist."

word = input("Enter the Word: ")
print(meaning(word))
