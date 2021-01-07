def cutoff_rank(scores, cutoff):
    scores_count = {}
    for s in scores:
        if s not in scores_count:
            scores_count[s] = 1
        else:
            scores_count[s] += 1
    result = 0
    for i, score in enumerate(sorted(scores_count, reverse=True), 1):
        i = max(i, result)
        if i >= cutoff or score == 0:
            return result
        result += scores_count[score]
    return result


if __name__ == "__main__":
    assert cutoff_rank([100, 50, 50, 25], 3) == 3
    assert cutoff_rank([100, 50, 50, 50, 25], 3) == 4
