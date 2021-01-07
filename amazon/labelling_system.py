"""
Given the original string label, construct a new string by rearranging the original string and deleting characters as needed.
Return the alphabetically-largest string that can be constructed respecting the limit
as to how many consecutive characters can be the same (represented by k).

"Alphabetically-largest" is defined in reverse alphabetical order
(e.g., b is "larger" than a, c is "larger" than b, etc.) from left to right (e.g., "ba" is larger than "ab").

Write an algorithm to return the alphabetically-largest string that can be constructed respecting the above limits.

Input
originalLabel : a string representing the original string label;
charlimit : an integer representing the maximum number of identical consecutive characters the new string can have k.

Output
Return a string representing the alphabetically largest string that can be constructed that has no more than k identical consecutive characters.
"""
import heapq


def labelling(original_label, char_limit):
    heap = [(-ord(c), c) for c in original_label]
    heapq.heapify(heap)
    result = ""
    while heap:
        o, c = heapq.heappop(heap)
        if result[-char_limit:] != c * char_limit:
            result += c
        else:
            tmp = [(o, c)]
            while heap and heap[0][1] == c:
                tmp.append(heapq.heappop(heap))
            if heap:
                result += heapq.heappop(heap)[1]
                [heapq.heappush(heap, i) for i in tmp]
    return result


if __name__ == "__main__":
    assert labelling("baccc", 2) == "ccbca"
    assert labelling("aaaaabccccddzzzzz", 2) == "zzdzzdzccbccaa"
