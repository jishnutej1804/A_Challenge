
def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort intervals by their starting values
    intervals = sorted(intervals, key=lambda interval: interval[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        previous = merged[-1]

        # Check whether the intervals overlap
        if current[0] <= previous[1]:
            previous[1] = max(previous[1], current[1])
        else:
            merged.append(current[:])

    return merged


# Test cases
print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(merge_intervals([[1, 4], [4, 5]]))
print(merge_intervals([[1, 10], [2, 3], [4, 8]]))
print(merge_intervals([]))
print(merge_intervals([[5, 7]]))
