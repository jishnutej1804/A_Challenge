from collections import Counter
import heapq


def top_k_frequent(nums, k):
    frequency = Counter(nums)

    min_heap = []

    for num, count in frequency.items():
        heapq.heappush(min_heap, (count, num))

        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return [num for count, num in min_heap]


print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))
print(top_k_frequent([1], 1))
print(top_k_frequent([4, 4, 4, 6, 6, 7, 7, 7], 2))
print(top_k_frequent([1, 2, 2, 3, 3, 3], 1))