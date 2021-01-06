"""
Return the key of the keypress that had the longest duration.
If there are multiple such keypresses, return the lexicographically largest key of the keypresses.

Input: releaseTimes = [9,29,49,50], keysPressed = "cbcd"
Output: "c"

Input: releaseTimes = [12,23,36,46,62], keysPressed = "spuda"
Output: "a"
"""


def slowest_key(release_times, keys_pressed: str) -> str:
    slowest_time = release_times[0]
    slowest_idx = 0
    for i, n in enumerate(release_times):
        if i == 0:
            continue
        time = n - release_times[i - 1]
        if time > slowest_time or (
            time == slowest_time and keys_pressed[i] > keys_pressed[slowest_idx]
        ):
            slowest_idx = i
            slowest_time = time
    return keys_pressed[slowest_idx]


if __name__ == "__main__":
    assert slowest_key([9, 29, 49, 50], "cbcd") == "c"
    assert slowest_key([12, 23, 36, 46, 62], "spuda") == "a"
