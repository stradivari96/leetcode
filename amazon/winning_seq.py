"""
The sequence must be strictly increasing at first and then strictly decreasing.

For example, [4, 5, 4, 3, 2] beats [3,4,5,4,3] because its first element is larger,
and [4, 5, 6, 5, 4] beats [4,5,4,3,2] because its third element is larger.
Given the length of the sequence and the range of integers, return the winning sequence.
If it is not possible to construct such a sequence, return -1.

The input to the function/method consists of three arguments:
num, an integer representing the size of sequence to create;
lowerEnd, an integer representing the lower end of integer range;
upperEnd, an integer representing the upper end of integer range.

Output
Return a list of integers representing the winning sequence and if the sequence is not possible then return a list with an integer -1.
"""


def winning(n, low, high):
    full_seq = list(range(low, high)) + list(range(high, low - 1, -1))
    if n > len(full_seq):
        return -1

    cut = (len(full_seq) // 2) - 1

    if len(full_seq[cut : cut + n]) < n:
        cut -= n - len(full_seq[cut : cut + n])
    return full_seq[cut : cut + n]


if __name__ == "__main__":
    assert winning(5, 3, 10) == [9, 10, 9, 8, 7]
    assert winning(7, 3, 10) == [9, 10, 9, 8, 7, 6, 5]
