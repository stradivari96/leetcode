"""
Given an int array nums and an int target, find how many unique pairs in the array
such that their sum is equal to target.

Return the number of pairs.

Input: nums = [1, 1, 2, 45, 46, 46], target = 47
Output: 2

Input: nums = [1, 1], target = 2
Output: 1
"""


def unique_pairs(nums, target):
    res = set()
    out = set()

    for value in nums:
        if target - value in res:
            out.add((value, target - value))
        else:
            res.add(value)

    return len(out)


if __name__ == "__main__":
    assert unique_pairs([1, 1, 2, 45, 46, 46], 47) == 2
    assert unique_pairs([1, 1], 2) == 1
