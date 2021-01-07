"""
The number of transactions in any given second cannot exceed 3.
The number of transactions in any given 10 second period cannot exceed 20.
A ten-second period includes all requests arriving from any time max(1, T-9) to T
(inclusive of both) for any valid time T.
The number of transactions in any given minute cannot exceed 60.
Similar to above, 1 minute is from max(1, T-59) to T.
Any request that exceeds any of the above limits will be dropped by the gateway.
Given the times at which different requests arrive sorted ascending,
write an algorithm to find how many requests will be dropped.

Input
num: an integer representing the number of requests;
requestTime: a list of integers representing the times of various requests.

Output
Return an integer representing the total number of dropped requests.
"""


def dropped_requests(requests):

    dropped = 0

    for i in range(len(requests)):
        if i > 2 and requests[i] == requests[i - 3]:
            dropped += 1
        elif i > 19 and requests[i] - requests[i - 20] < 10:
            dropped += 1
        elif i > 59 and requests[i] - requests[i - 60] < 60:
            dropped += 1

    return dropped


if __name__ == "__main__":
    assert (
        dropped_requests(
            [
                1,
                1,
                1,
                1,
                2,
                2,
                2,
                3,
                3,
                3,
                4,
                4,
                4,
                5,
                5,
                5,
                6,
                6,
                6,
                7,
                7,
                7,
                7,
                11,
                11,
                11,
                11,
            ]
        )
        == 7
    )
