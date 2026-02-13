counts = {}

with open("book.txt") as f:
    for line in f:
        for word in line.split():
            counts[word] = counts.get(word, 0) + 1

bigcount, bigword = None, None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount, bigword = count, word

print(bigword, bigcount)
