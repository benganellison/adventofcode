#! /usr/bin/env python
import math


def main(i):
    l = i.splitlines()
    r = len(l)
    n = []
    s = []
    o = None

    for c in range(len(l[-1])):
        if l[-1][c] in ("*", "+"):
            if o and o == "*":
                s.append(math.prod(n))
            elif o and o == "+":
                s.append(sum(n))
            o = l[-1][c]
            n = []

        m = 0
        for w in range(r - 1):
            m = int(str(m) + str(l[w][c]))
        if m > 0:
            n.append(m)
    else:
        if o and o == "*":
            s.append(math.prod(n))
        elif o and o == "+":
            s.append(sum(n))

    return sum([x for x in s if x is not None])


if __name__ == "__main__":
    with open("input.txt") as f:
        i = f.read()

    print("final result: ", main(i))
