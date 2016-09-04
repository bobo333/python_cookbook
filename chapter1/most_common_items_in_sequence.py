from collections import Counter

words = "look into my eyes look into my eyes the eyes the eyes not around the eyes don't look around my eyes " \
        "look into my eyes you're under".split()

word_counts = Counter(words)

top_3 = word_counts.most_common(3)
print(top_3)

# can be interacted with directly
more_words = "why are you not looking into my eyes".split()

for word in more_words:
    word_counts[word] += 1

print(word_counts["eyes"])

# can be combined like arithmetic
a = Counter(words)
b = Counter(more_words)

print(a)
print(b)

c = a + b

print(c)

d = a - b
print(d)
