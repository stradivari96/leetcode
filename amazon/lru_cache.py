def lru_cache_misses(pages, max_cache_size):
    cache = set()
    queue = []
    misses = 0

    for p in pages:
        if p not in cache:
            cache.add(p)
            queue.append(p)
            if len(queue) > max_cache_size:
                cache.remove(queue.pop(0))
            misses += 1
        else:
            queue.remove(p)
            queue.append(p)
    return misses


if __name__ == "__main__":
    assert lru_cache_misses([1, 2, 1, 3, 1, 2], 2) == 4
