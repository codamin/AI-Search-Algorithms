import heapq

class Fringe:
    def __init__(self):
        self.container = []

    def isEmpty(self):
        return len(self.container) == 0
class FringeBFS(Fringe):

    def push(self, problem, accessPath):
        self.container.append(Node(problem, accessPath))

    def pop(self):
        return self.container.pop(0)
        
class FringeDFS(Fringe):

    def push(self, problem, accessPath):
        self.container.insert(0, Node(problem, accessPath))

    def pop(self):
        return self.container.pop()


class FringeAstar(Fringe):
    def __init__(self):
        Fringe.__init__(self)
        heapq.heapify(self.container)
        self.stateDict = {}

    def isInFringe(self, node):
        return node in self.container

    def push(self, problem, accessPath, accessCost = 0, totalCost = 0):
        node = aStarNode(problem, accessPath, accessCost, totalCost)
        if self.isInFringe(node):
            self.stateDict[node.state].marked = True
            
        self.stateDict[node.state] = node
        heapq.heappush(self.container, node)
 
    def pop(self):
        while(self.container):
            poppedNode = heapq.heappop(self.container)
            if not poppedNode.marked:
                return poppedNode

class Node:
    def __init__(self, state, accessPath):
        self.state = state
        self.accessPath = accessPath

class aStarNode(Node):
    def __init__(self, state, accessPath, accessCost, totalCost):
        Node.__init__(self, state, accessPath)
        self.accessCost = accessCost
        self.totalCost = totalCost
        self.marked = False
    
    def __hash__(self):
        return hash(self.state)

    def __eq__(self,other):
        return self.state == other.state
        
    def __lt__(self, other):
        return self.totalCost < other.totalCost