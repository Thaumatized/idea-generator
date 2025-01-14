import json
import random

wordsFile = open("words.json")
words = json.load(wordsFile)

print(random.choice(words["adjectives"]) + " " + random.choice(words["structures"]))