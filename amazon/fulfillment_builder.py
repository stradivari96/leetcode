"""
Merge two parts until the product is complete.
The time to combine two parts is the sum of the two sizes.

Input: parts - list of integers
Return: time - integer
"""
import heapq


def building_parts(parts):
    if len(parts) == 1:
        return 0
    time = 0
    heapq.heapify(parts)  # O(n) space
    while len(parts) > 1:  # O(logn) time
        p1 = heapq.heappop(parts)  # O(logn) time
        p2 = heapq.heappop(parts)
        t = p1 + p2
        heapq.heappush(parts, t)
        time += t
    return time


if __name__ == "__main__":
    assert building_parts([8, 4, 6, 12]) == 58
