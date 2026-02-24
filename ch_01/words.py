file_path = "./book.txt"

counts = {}
with open(file_path) as handle:
    for line in handle:
        for word in line.split():
            counts[word] = counts.get(word, 0) + 1

bigcount, bigword = None, None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount, bigword = count, word

print(bigword, bigcount)
