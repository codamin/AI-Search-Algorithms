class State:
    def __init__(self, snake, foods):
        self.snake = snake
        self.foods = foods
    
    def __str__(self):
        return("{} ## {}".format(self.snake, self.foods))

    def __hash__(self):
        return hash((tuple(self.snake)))

    def __eq__(self,other):
        if isinstance(other, self.__class__):
            # Ignoring .b attribute
            # return self.snake == other.snake and self.foods == other.foods
            return self.snake == other.snake
        else:
            return NotImplemented

class Node:
    def __init__(self, state, accessPath):
        self.state = state
        self.accessPath = accessPath

class aStarNode(Node):
    def __init__(self, state, accessPath, accessCost = 0, totalCost = 0):
        Node.__init__(self, state, accessPath)
        self.accessCost = accessCost
        self.marked = False
    
    def __hash__(self):
        return hash(self.state)

    def __eq__(self,other):
        return self.state == other.state
        
    def __lt__(self, other):
        return self.accessCost < other.accessCost


x = State([(0, 0)] , [(3, 1, 1), (3, 2, 1), (1, 4, 2), (4, 3, 1)])
y = State([(0, 0)] , [(3, 1, 2), (3, 2, 1), (1, 4, 2), (4, 3, 1)])
n1 = aStarNode(x, [], 0, 10)
n2 = aStarNode(x, [], 0, 20)
d = {}
d[x] = n1

z = set()
z.add(n1)
print(n2 in z)
d[n2.state].state = (20,21)
print(n2.state)