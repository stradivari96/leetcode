def earliest_time(opening_times, offload_times):
    opening_times = sorted(opening_times)
    offload_times = sorted(offload_times, reverse=True)
    times = [
        max([time + o for o in offload_times[4 * i : 4 * i + 4]])
        for i, time in enumerate(opening_times)
    ]

    return max(times)


if __name__ == "__main__":
    assert earliest_time([8, 10], [2, 2, 3, 1, 8, 7, 4, 5]) == 16
