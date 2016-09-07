import unicodedata

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'

print(s1)
print(s2)

print(s1 == s2)
print(len(s1))
print(len(s2))

# \u00f1 is literally n with a ~, in one character
# \u0303 is just the ~ character, separate from the n, making the 2nd string longer and different from the first

# since the strings really should be the same, they should be normalized:
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1 == t2)
print(t1, t2)
print(ascii(t1), ascii(t2))
print()

t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print(t3 == t4)

print(t3, t4)
print(ascii(t3), ascii(t4))

# NFC is for normalizing characters to be Fully Composed, meaning use one code-point if possible (ex: n with ~ on it)
# NFD means normalizing characters Fully Decomposed, so using multiple characters (ex: n followed by a separate ~)

# NFKC and NFKD are other normalization forms that add extra compatibility for certain kinds of characters
# ex:
s = '\ufb01'    # A single character
print(s)        # prints what looks like "fi" despite being one character
print(len(s))
s_1 = unicodedata.normalize('NFKD', s)
print(s_1)      # Gets broken into 2 separate characters now
print(len(s_1))
s_2 = unicodedata.normalize('NFKC', s)
print(s_2)      # Also broken into 2 separate characters
print(len(s_2))
print()

# unicodedata can also remove "diacritical marks"
t_1 = unicodedata.normalize('NFD', s1)
t_1t = ''.join(c for c in t_1 if not unicodedata.combining(c))
print(t_1t)

t_2 = unicodedata.normalize('NFD', s2)
t_2t = ''.join(c for c in t_2 if not unicodedata.combining(c))
print(t_2t)

# unicodedata.combining tests each character to see if it's a "combining" character, meaning it will get joined with
# whatever character precedes it (like the ~ following an n gets combined into one character). Therefore, it's important
# to normalize with NFD so the combining characters are fully decomposed and exist as separate characters to be tested.
t_3 = unicodedata.normalize('NFC', s1)
t_3t = ''.join(c for c in t_3 if not unicodedata.combining(c))
print(t_3t)
