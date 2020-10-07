# x = State([(0, 0)] , [(3, 1, 1), (3, 2, 1), (1, 4, 2), (4, 3, 1)])
# y = State([(0, 0)] , [(3, 1, 2), (3, 2, 1), (1, 4, 2), (4, 3, 1)])
# n1 = aStarNode(x, [], 0, 10)
# n2 = aStarNode(x, [], 0, 20)

# print(hash(x))
import heapq
l = [[8,1,10], [7,5,10]]
p = [1,2,3]
# s = set()
# s.add(tuple(p))

heapq.heapify(l)
print(heapq.heappop(l))