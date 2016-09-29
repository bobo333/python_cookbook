import random
import ssl

values = [1, 2, 3, 4, 5, 6]
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print()

print(random.sample(values, 2))
print(random.sample(values, 2))
print(random.sample(values, 2))
print()

# random.shuffle shuffles values in place
random.shuffle(values)
print(values)
random.shuffle(values)
print(values)
print()

# random.randint gives integers at random
print(random.randint(0, 10))
print(random.randint(0, 10))
print(random.randint(0, 10))
print()

# random.random gives uniform floating point values between 0 and 1
print(random.random())
print(random.random())
print(random.random())
print()

# N random bits expressed as an integer
print(random.getrandbits(1))
print(random.getrandbits(1))
print(random.getrandbits(1))
print(random.getrandbits(1))
print(random.getrandbits(5))
print(random.getrandbits(50))
print()

# python uses Mersenne Twister algorithm for randoms, which is deterministic. However, the initial seed can be changed
random.seed()               # set seed based on system time or os.urandom()
random.seed(12345)          # seed based on provided integer
random.seed(b'bytedata')    # seed from byte data
print()

# random.uniform() produces uniformly distributed numbers
print(random.uniform(0, 10))
print()

# note: the random module should not be used for cryptography since it's not truly random. For cryptographic purposes
# consider using the ssl module instead
x = ssl.RAND_bytes(5)
print(x)
print(int.from_bytes(x, 'little'))
print(int.from_bytes(x, 'big'))
