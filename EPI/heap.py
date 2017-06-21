import heapq
import itertools


# Sort approximately k-sorted array
def sort_approximately_sorted_array(sequence, k):
    min_heap = []
    for x in itertools.islice(sequence, k):
        heapq.heappush(min_heap, x)

    for x in sequence:
        smallest = heapq.heappushpop(min_heap, x)
        print(smallest)
        result.append(smallest)

    while min_heap:
        smallest = heapq.heappop(min_heap)
        print(smallest)
        result.append(smallest)

def simple_test():
    A = [2, 1, 5, 4, 3, 9, 8, 7, 6]
    sort_approximately_sorted_array(iter(A), 3)
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9]

