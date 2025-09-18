import heapq

li = [25, 20, 15, 30, 40]

# Convert the list into a heap
heapq.heapify(li)
print("Heap queue:", li)  # Heap queue: [15, 20, 25, 30, 40]

# Using Heap as a Max-Heap
# By default, Python’s heapq implements a min-heap. To create a max-heap
#  you can simply invert the values (store negative numbers).

# Example: Below example, convert a list into a max-heap by storing
# negative numbers and then retrieve the largest element:

import heapq

nums = [10, 20, 15, 30, 40]
print(nums)

mx_heap = [-n for n in nums]
print(f"before : {mx_heap}")
heapq.heapify(mx_heap)
print(f"after : {mx_heap}")


print(f"max heap element : ", -mx_heap[0])


print(f"\n\nAppending and Popping Elements\n")

# heapq.heappush(heap, item) adds a new element to the heap.
# heapq.heappop(heap) removes and returns the smallest element.

h = [10, 40, 25, 15, 20]

heapq.heapify(h)
print(f"\nh before = {h}")  # h = [10, 15, 25, 40, 20]

# appending
heapq.heappush(h, 5)
print(f"h after = {h}")  # h after = [5, 15, 10, 40, 20, 25]

# pop smallest eliment
min = heapq.heappop(h)
print(f"smallest : {min}")


print(f"\n\n Appending and Popping Simultaneously\n")

# heapq.heappushpop() function efficiently pushes a new element onto the heap and pops
#  the smallest one in a single step.
print(f"\n\nheapq.heappushpop()\n")
h2 = [10, 20, 15, 30, 40]
heapq.heapify(h)
print(f"h before : {h}")
min2 = heapq.heappushpop(h, 25)
print(f"h : {h}")  # h : [15, 20, 25, 40, 25]

print(f"small 2 : {min2}")


print(f"\n\nFinding Largest and Smallest Elements\n\nnlargest() and nsmallest()\n")

# heapq.nlargest(n, iterable) returns the n largest elements from the iterable.
# heapq.nsmallest(n, iterable) returns the n smallest elements from the iterable.


h3 = [10, 30, 25, 40, 35]
heapq.heapify(h3)

maxh3 = heapq.nlargest(3, h3)
print(f"max 3 nums : {maxh3}")
max_h3 = heapq.nsmallest(3, h3)
print(f"min 3 nums : {max_h3}")


print(f"\n\nReplace Operation\n\nheapq.heapreplace()\n\n")

# It returns the smallest element before replacing it.
# It is more efficient than using heappop() followed by
#  heappush() because it performs both operations in one step


h4 = [10, 20, 15, 30, 40]
heapq.heapify(h4)
print(f"before removed min num : {h4}")

min3 = heapq.heapreplace(h4, 5)
print(f"after removed min num : {h4}")

print(f"removed min num : {min3}")


print(f"\n\nMerge Operation  :  heapq.merge()\n ")

print(f"before merging : {h4}")
h5 = [2, 4, 6, 8]
h6 = list(heapq.merge(h4, h5))
print(f"after merging : {h6}")


# ✅ Simple Advantages of heapq
# Fast for priority tasks Quickly adds and removes items based on priority.

# Memory-efficient Uses less memory than some other data structures.

# Easy to use Comes with built-in functions like heapify, heappush, and heappop.

# Good for many use cases Works well for things like heaps and priority queues.


# ❌ Simple Disadvantages of heapq
# Not good for complex operations Doesn’t support advanced data manipulation easily.

# No middle access You can’t directly access items in the middle of the heap.

# Doesn’t fully sort Only keeps the smallest item at the top, not a full sort.

# Not thread-safe Can cause issues if used in multi-threaded programs without extra care.
