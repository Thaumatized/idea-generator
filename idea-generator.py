import json
import random

wordsFile = open("words.json")
words = json.load(wordsFile)

categories = []
for key in words:
    if key != "adjectives":
        categories.append(key)

print("Pick a category")
index = 0
for key in categories:
    print(str(index) + ": " + key)
    index += 1

index = -1
while index < 0 or index > len(categories):
    try:
        index = int(input())
    except:
        pass

print(random.choice(words["adjectives"]) + " " + random.choice(words[categories[index]]))