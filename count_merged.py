# merged.txt ka lines, words, chars count nikalna

with open("merged.txt", "r", encoding="utf-8") as f:
    data = f.read()

# Lines count
lines = data.split("\n")
line_count = len(lines)

# Words count
words = data.split()
word_count = len(words)

# Characters count
char_count = len(data)

print("Lines:", line_count)
print("Words:", word_count)
print("Characters:", char_count)
