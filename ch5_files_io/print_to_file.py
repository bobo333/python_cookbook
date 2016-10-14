with open('ex_files/print_to_me.txt', 'w') as f:
    print('some tasty tasty text!', file=f)


with open('ex_files/print_to_me.txt') as f:
    print(f.read())


# opening in binary mode can do weird things, make sure to use text mode (t, the default)
