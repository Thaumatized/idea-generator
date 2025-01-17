import json
import random

wordsFile = open("words.json")
words = json.load(wordsFile)

print("Should verbs count as adjectives? eg. quenching [y/n]")
verbsAsAdjectives = False
while True:
    try:
        string = input().lower()
        if(string == "y"):
            verbsAsAdjectives = True
            break
        if(string == "n"):
            verbsAsAdjectives = False
            break
    except:
        pass

categories = []
for key in words:
    if key == "adjectives":
        continue
    if key == "activities" and verbsAsAdjectives:
        continue
    categories.append(key)

print("Pick a category")
index = 0
for key in categories:
    print(str(index) + ": " + key)
    index += 1

print(str(index) + ": random")

index = -1
while index < 0 or index > len(categories) + 1:
    try:
        index = int(input())
    except:
        pass
if(index == len(categories)):
    index = random.randint(0, len(categories) - 1)

print("Pick adjective count")
adjectiveCount = 0
while adjectiveCount <= 0:
    try:
        adjectiveCount = int(input())
    except:
        pass

adjectives = words["adjectives"] if not verbsAsAdjectives else [*words["adjectives"], *words["activities"]]

for i in range(adjectiveCount):
    print(random.choice(adjectives), end=" ")
          
print(random.choice(words[categories[index]]))