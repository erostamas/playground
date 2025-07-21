import heapq

#heap is a binary heap that is a binary tree that has all leaves filled from left to right - complete binary tree
#       2
#     /   \
#    4     6
#   / \   /
#  8  10  12
#
#use when min/max or k min/max problems occur
#heapify list takes O(n)
#min/max is always on index 0 so its O(1)
#heappush and heappop are O(logn)

heap = []

heapq.heappush(heap, 50)
heapq.heappush(heap, 10)

print(heap)

lists = [
    [1, 4, 5],
    [1, 3, 4],
    [2, 6]
]

merged_and_sorted = []
for l in lists:
    heapq.heapify(l)
for 