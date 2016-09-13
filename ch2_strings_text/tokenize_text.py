from collections import namedtuple
import re

# tokenize this text:
text = 'foo = 23 + 42 * 10'

# first define all possible types of tokens with regexes:
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

# order matters, longer patterns need to go first or the scanner will have problems
master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

# next use the scanner method of regex pattern object. Ex:
scanner = master_pat.scanner('foo = 42')    # scanner seems to be undocumented?
print(scanner.match())
print()

Token = namedtuple('Token', ['type', 'value'])


def generate_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())


for tok in generate_tokens(master_pat, 'foo = 42'):
    print(tok)

print()

# can filter the token stream as well
tokens = (tok for tok in generate_tokens(master_pat, text) if tok.type != 'WS')
for tok in tokens:
    print(tok)
