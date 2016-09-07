import re

# . matches any character *except* newlines

# ex for matching C-style comments
comment1 = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a
              multiline comment */'''

print(comment1.findall(text1))
print(comment1.findall(text2))
print()

# one solution is to explicitly add in new-line support with a non-capturing group
comment2 = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment2.findall(text2))

# the re module also has re.DOTALL, which makes the . match all characters *including* newlines
comment3 = re.compile(r'/\*(.*?)\*/', flags=re.DOTALL)
print(comment3.findall(text2))

# this can add complications with more complex regexes, so it's often a better idea to craft the regex in a way that
# doesn't require extra flags
