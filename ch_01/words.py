words = {}

with open("words.txt") as f:
    total = [w.strip() for w in f.read().split()]

for item in total:
    words[item] = words.get(item, 0) + 1


