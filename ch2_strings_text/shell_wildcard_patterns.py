from fnmatch import fnmatch, fnmatchcase

# these functions provide support for shell-style pattern matching

print(fnmatch("foo.txt", "*.txt"))
print(fnmatch("foo.txt", "?oo.txt"))
print(fnmatch("foo.txt", "*.jpg"))

print(fnmatch("hello1234.txt", "*[0-9].txt"))

# case-sensitivity is OS specific, but fnmatchcase will always be case-sensitive
print(fnmatch("foo.txt", "*.TXT"))
print(fnmatchcase("foo.txt", "*.TXT"))
