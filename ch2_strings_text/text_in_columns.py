import textwrap
import os

s = "42 (forty-two) is the natural number that succeeds 41 and precedes 43. 42 is the atomic number of molybdenum. In" \
    " 1966, mathematician Paul Cooper theorized that the fastest, most efficient way to travel across continents " \
    "would be to bore a straight hollow tube directly through the Earth, connecting a set of antipodes, remove the " \
    "air from the tube and fall through. The first half of the journey consists of free-fall acceleration, while " \
    "the second half consists of an exactly equal deceleration. The time for such a journey works out to be 42 " \
    "minutes. Even if the tube does not pass through the exact center of the Earth, the time for a journey powered " \
    "entirely by gravity (known as a gravity train) always works out to be 42 minutes, so long as the tube remains " \
    "friction-free, as while the force of gravity would be lessened, the distance traveled is reduced at an equal " \
    "rate. (The same idea was proposed, without calculation by Lewis Carroll in 1893 in Sylvie and Bruno Concluded.)"

print(textwrap.fill(s, 40))
print()
print(textwrap.fill(s, 40, initial_indent='    '))
print()
print(textwrap.fill(s, 40, subsequent_indent='    '))
print()

term_size = os.get_terminal_size().columns      # might fail in pycharm
print(textwrap.fill(s, term_size))
