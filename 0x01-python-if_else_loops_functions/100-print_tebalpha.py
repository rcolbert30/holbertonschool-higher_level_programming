#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    if (i % 2 != 0):
        r = i - ord('a') + ord('A')
    else:
        r = i
    print("{:c}".format(r), end="")
