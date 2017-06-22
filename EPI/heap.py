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


class Star:

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    @property
    def distance(self):
        return self.x**2 + self.y**2 + self.z**2

    def __lt__(self, rhs):
        return self.distance < rhs.distance

    def __str__(self):
        return ' '.join(map(str, (self.x, self.y, self.z)))

    def __eq__(self, rhs):
        return math.isclose(self.distance, rhs.distance)

# note since we need to implement max heap we are using negative of what we are storing 
# as heap in by default min heap
def find_closest_k_stars(k, stars):
    max_heap = []
    reader = csv.reader(stars)
    for line in reader:
        star = Star(*map(float, line))
        heapq.heappush(max_heap, (-star.distance, star))
        if len(max_heap) == k + 1:
            heapq.heappop(max_heap)
    return [s[1] for s in heapq.nlargest(k, max_heap)]



global_result = []
def online_median(sequence):
    # min_heap stores the larger half seen so far.
    min_heap = []
    # max_heap stores the smaller half seen so far values in max_heap are negative
    max_heap = []

    for x in sequence:
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, x))
        # Ensure min_heap and max_heap have equal number of elements if an even
        # number of elements is read; otherwise, min_heap must have one more
        # element than max_heap.
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        print(0.5 * (min_heap[0] + (-max_heap[0]))
              if len(min_heap) == len(max_heap) else min_heap[0])