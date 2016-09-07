import re

pat1 = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print(pat1.findall(text1))

text2 = 'Computer says "no." Phone says "yes."'
print(pat1.findall(text2))

# adding a ? after the * in the regex makes it "non-greedy," producing the shortest match possible instead of the
# longest
pat2 = re.compile(r'\"(.*?)\"')
print(pat2.findall(text2))
