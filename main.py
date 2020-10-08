from agent import *
from foodProblem import *
from search import *

foodProblem = FoodSearchProblem('tests/test3.txt')

# bfsAgent = Agent(foodProblem, graphSearch)
# bfsAgent.search(searchType='bfs')

# idsAgent = Agent(foodProblem, ids)
# idsAgent.search(maxDepth = 50)


idsAgent = Agent(foodProblem, graphSearch)
idsAgent.search(searchType='aStar', heuristic = lambda x : 0)