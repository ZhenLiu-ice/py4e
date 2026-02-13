words = {}

with open("words.txt") as f:
    total = [w.strip() for w in f.read().split()]

common = ""
max = 0
for item in total:
    words[item] = words.get(item, 0) + 1
    if words[item] > max:
        common, max = item, words[item]

print(common)
