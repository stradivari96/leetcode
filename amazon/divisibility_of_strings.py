"""
Given 2 strings s and t.
Search for the smallest string x
that if concatenated any number of times, we get
both s and t.

return the len of x
size(t) <= size(s)
"""


def divisibility(s, t):
    if len(s) % len(t) != 0:
        return -1
    for i in range(len(s)):
        if s[i] != t[i % len(t)]:
            return -1

    for i in range(len(t)):
        j = 0
        for j in range(len(t)):
            if t[j] != t[j % (i + 1)]:
                break
        if j == len(t) - 1:
            return i + 1
    return -1


if __name__ == "__main__":
    assert divisibility("bcdbcdbcd", "bcdbcd") == -1
    assert divisibility("bcdbcdbcdbcd", "bcdbcd") == 3
