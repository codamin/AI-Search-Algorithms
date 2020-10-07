import heapq

class Fringe:
    def __init__(self):
        self.container = []

    def isEmpty(self):
        return len(self.container) == 0
class FringeBFS(Fringe):
    def push(self, state, accessPath):
        node = (state, accessPath)
        self.container.append(node)

    def pop(self):
        return self.container.pop(0)
        
class FringeDFS(Fringe):
    def push(self, state, accessPath):
        node = (state, accessPath)
        self.container.insert(0, node)

    def pop(self):
        return self.container.pop()


class FringeAstar(Fringe):
    def __init__(self):
        Fringe.__init__(self)
        heapq.heapify(self.container)
        self.queueNodes = {}
        self.counter = 0

    def mustUpdate(self, state, totalCost):
        return state in self.queueNodes and  totalCost < self.queueNodes[state][0]

    def push(self, state, accessPath, accessCost = 0, totalCost = 0):
        if self.mustUpdate(state, totalCost):
            self.queueNodes[state][-1] = True

        self.counter += 1
        node = [totalCost, self.counter, state, accessPath, accessCost, False]
        self.queueNodes[state] = node
        heapq.heappush(self.container, node)
 
    def pop(self):
        while(self.container):
            poppedNode = heapq.heappop(self.container)
            if not poppedNode[-1]:
                return poppedNode[2:5]