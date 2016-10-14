# can control what new lines get translated to, useful when opening files written on systems that use different default
# new line characters (windows uses \n\r vs \n for unix)

# normal
with open('../.gitignore') as f:
    print(f.readline())
print('done reading\n')

# disabling translation
with open('../.gitignore', newline='') as f:
    print(f.readline())
print('done reading')


# handling encodings (file is actually utf-8, so ascii would throw an exception if errors are not handled)
# replace unknown characters with question marks
with open('ex_files/non_ascii.txt', encoding='ascii', errors='replace') as f:
    print(f.read())

# ignore unknown characters entirely
with open('ex_files/non_ascii.txt', encoding='ascii', errors='ignore') as f:
    print(f.read())
