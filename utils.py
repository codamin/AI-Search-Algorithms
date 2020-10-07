import heapq

class Fringe:
    def __init__(self):
        self.container = []
        self.states = set()

    def isEmpty(self):
        return len(self.container) == 0

class FringeBFS(Fringe):
    def push(self, state, parent, action, depth, g_n, f_n):
        node = (state, parent, action, depth, g_n, f_n)
        if state in self.states:
            return False      
        self.container.append(node)
        self.states.add(state)
        return True

    def pop(self):
        poppedNode = self.container.pop(0)
        self.states.remove(poppedNode[0])
        return poppedNode
        
class FringeDFS(Fringe):
    def push(self, state, parent, action, depth, g_n, f_n):
        node = (state, parent, action, depth, g_n, f_n)
        if state in self.states:
            return False   
        self.container.insert(0, node)
        self.states.add(state)
        return True

    def pop(self):
        poppedNode = self.container.pop()
        self.states.remove(poppedNode[0])
        return poppedNode


class FringeAstar(Fringe):
    def __init__(self):
        Fringe.__init__(self)
        heapq.heapify(self.container)
        self.queueNodes = {}
        self.counter = 0

    def mustUpdate(self, state, totalCost):
        return state in self.queueNodes and  totalCost < self.queueNodes[state][0]

    def push(self, state, parent, action, depth, g_n = 0, f_n = 0):
        didPush = True
        if self.mustUpdate(state, f_n):
            self.queueNodes[state][-1] = True
            didPush = False

        self.counter += 1
        node = [f_n, self.counter, state, parent, action, depth, g_n, False]
        self.queueNodes[state] = node
        heapq.heappush(self.container, node)
        return didPush

    def pop(self):
        while(self.container):
            poppedNode = heapq.heappop(self.container)
            if not poppedNode[-1]:
                return poppedNode[2:7] + [poppedNode[0]]